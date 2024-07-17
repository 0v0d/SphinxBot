const { SlashCommandBuilder } = require('discord.js');

module.exports = {
    data: new SlashCommandBuilder()
        .setName('decorate')
        .setDescription('コードを装飾します')
        .addStringOption(option =>
            option.setName('language')
                .setDescription('プログラミング言語を選択')
                .setRequired(true)
                .addChoices(
                    { name: 'Python', value: 'py' },
                    { name: 'C++', value: 'cpp' },
                    { name: 'C#', value: 'cs' },
                    { name: 'Java', value: 'java' },
                    { name: 'TypeScript', value: 'ts' },
                    { name: 'JavaScript', value: 'js' },
                    { name: 'Markdown', value: 'md' },
                    { name: 'Diff', value: 'diff' }
                ))
        .addStringOption(option =>
            option.setName('code')
                .setDescription('装飾するコード')
                .setRequired(true)),
    async execute(interaction) {
        const language = interaction.options.getString('language');
        const code = interaction.options.getString('code');

        await interaction.reply(`\`\`\`${language}\n${code}\n\`\`\``);
    },
};