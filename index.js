require('dotenv').config()
const fs = require('fs').promises;
const path = require('path');
const { Client, Collection, Events, GatewayIntentBits } = require('discord.js');

const token = process.env.DISCORD_TOKEN;

const client = new Client({ intents: [GatewayIntentBits.Guilds] });
client.commands = new Collection();

async function loadCommands() {
    const commandsPath = path.join(__dirname, 'commands');
    const commandFiles = await fs.readdir(commandsPath);

    for (const file of commandFiles) {
        if (file.endsWith('.js')) {
            const filePath = path.join(commandsPath, file);
            const command = require(filePath);
            if ('data' in command && 'execute' in command) {
                client.commands.set(command.data.name, command);
            } else {
                console.log(`[警告] ${filePath} のコマンドには必要なプロパティがありません。`);
            }
        }
    }
}

client.once(Events.ClientReady, (c) => {
    console.log(`準備OKです! ${c.user.tag}がログインします。`);
});

client.on(Events.InteractionCreate, async (interaction) => {
    if (!interaction.isChatInputCommand()) return;

    const command = client.commands.get(interaction.commandName);

    if (!command) {
        await interaction.reply({ content: `${interaction.commandName}というコマンドには対応していません。`, ephemeral: true });
        return;
    }

    try {
        await command.execute(interaction);
    } catch (error) {
        console.error(error);
        const errorMessage = '申し訳ありませんが、コマンドの実行中にエラーが発生しました。';
        if (interaction.replied || interaction.deferred) {
            await interaction.followUp({ content: errorMessage, ephemeral: true });
        } else {
            await interaction.reply({ content: errorMessage, ephemeral: true });
        }
    }
});

async function main() {
    try {
        await loadCommands();
        await client.login(token);
    } catch (error) {
        console.error('ボットの起動中にエラーが発生しました:', error);
    }
}

main();