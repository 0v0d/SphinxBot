const { SlashCommandBuilder } = require('discord.js');

module.exports = {
    data: new SlashCommandBuilder()
        .setName('calc')
        .setDescription('計算機能')
        .addSubcommand(subcommand =>
            subcommand
                .setName('add')
                .setDescription('加算')
                .addNumberOption(option => option.setName('a').setDescription('1つ目の数値').setRequired(true))
                .addNumberOption(option => option.setName('b').setDescription('2つ目の数値').setRequired(true)))
        .addSubcommand(subcommand =>
            subcommand
                .setName('sub')
                .setDescription('減算')
                .addNumberOption(option => option.setName('a').setDescription('1つ目の数値').setRequired(true))
                .addNumberOption(option => option.setName('b').setDescription('2つ目の数値').setRequired(true)))
        .addSubcommand(subcommand =>
            subcommand
                .setName('mul')
                .setDescription('乗算')
                .addStringOption(option => option.setName('a').setDescription('1つ目の値').setRequired(true))
                .addStringOption(option => option.setName('b').setDescription('2つ目の値').setRequired(true)))
        .addSubcommand(subcommand =>
            subcommand
                .setName('div')
                .setDescription('除算')
                .addNumberOption(option => option.setName('a').setDescription('1つ目の数値').setRequired(true))
                .addNumberOption(option => option.setName('b').setDescription('2つ目の数値').setRequired(true)))
        .addSubcommand(subcommand =>
            subcommand
                .setName('mod')
                .setDescription('商算')
                .addNumberOption(option => option.setName('a').setDescription('1つ目の数値').setRequired(true))
                .addNumberOption(option => option.setName('b').setDescription('2つ目の数値').setRequired(true))),

    async execute(interaction) {
        const subcommand = interaction.options.getSubcommand();
        const a = interaction.options.getNumber('a') || interaction.options.getString('a');
        const b = interaction.options.getNumber('b') || interaction.options.getString('b');

        const ZERO_DIVISION_ERROR_MESSAGE = "0で割ることはできません。別の数値を入力してください。";

        switch (subcommand) {
            case 'add':
                await interaction.reply(`結果は${a + b}`);
                break;
            case 'sub':
                await interaction.reply(`結果は${a - b}`);
                break;
            case 'mul':
                await interaction.reply(`結果は${a * b}`);
                break;
            case 'div':
                if (b === 0) {
                    await interaction.reply(ZERO_DIVISION_ERROR_MESSAGE);
                } else {
                    await interaction.reply(`結果は${a / b}`);
                }
                break;
            case 'mod':
                if (b === 0) {
                    await interaction.reply(ZERO_DIVISION_ERROR_MESSAGE);
                } else {
                    await interaction.reply(`結果は${a % b}`);
                }
                break;
        }
    },
};