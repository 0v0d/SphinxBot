require('dotenv').config();
const { REST, Routes } = require('discord.js');
const fs = require('fs').promises;
const path = require('path');

const APPLICATION_ID = process.env.APPLICATION_ID;
const GUILD_ID = process.env.GUILD_ID;
const DISCORD_TOKEN = process.env.DISCORD_TOKEN;

async function loadCommands() {
    const commandsPath = path.join(__dirname, 'commands');
    const commandFiles = await fs.readdir(commandsPath);

    return Promise.all(
        commandFiles
            .filter(file => file.endsWith('.js'))
            .map(async file => {
                const command = require(path.join(commandsPath, file));
                return command.data.toJSON();
            })
    );
}

async function registerCommands(commands) {
    const rest = new REST({ version: '10' }).setToken(DISCORD_TOKEN);

    try {
        console.log('コマンドの登録を開始します...');
        await rest.put(
            Routes.applicationGuildCommands(APPLICATION_ID, GUILD_ID),
            { body: commands }
        );
        console.log('サーバー固有のコマンドが正常に登録されました！');
    } catch (error) {
        console.error('コマンドの登録中にエラーが発生しました:', error);
        throw error;
    }
}

async function main() {
    try {
        const commands = await loadCommands();
        await registerCommands(commands);
    } catch (error) {
        console.error('予期せぬエラーが発生しました:', error);
    }
}

main();
