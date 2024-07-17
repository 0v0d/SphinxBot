const { SlashCommandBuilder } = require("discord.js");

module.exports = {
    data: new SlashCommandBuilder()
        .setName("random")
        .setDescription("ランダムな数字を生成")
        .addIntegerOption(option =>
            option.setName("min")
                .setDescription("最小値")
                .setRequired(true))
        .addIntegerOption(option =>
            option.setName("max")
                .setDescription("最大値")
                .setRequired(true)),
    execute: async function (interaction) {
        const min = interaction.options.getInteger("min");
        const max = interaction.options.getInteger("max");

        if (min >= max) {
            return await interaction.reply("最小値は最大値より小さくしてください");
        }

        const randomNumber = Math.floor(Math.random() * (max - min + 1)) + min;
        await interaction.reply(randomNumber);
    }
};