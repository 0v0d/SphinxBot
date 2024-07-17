const {SlashCommandBuilder} = require("discord.js");
const axios = require("axios");

const url = "https://www.jma.go.jp/bosai/forecast/data/forecast/";
const json = ".json";
const locationMap = {
    "大阪": "270000",
    "奈良": "290000",
    "三重": "240000",
};

module.exports = {
    data: new SlashCommandBuilder()
        .setName("weather")
        .setDescription("天気情報")
        .addStringOption(option =>
            option.setName("location")
                .setDescription("場所を選択してください")
                .setRequired(true)
                .addChoices(
                    {name: "大阪", value: "大阪"},
                    {name: "奈良", value: "奈良"},
                    {name: "三重", value: "三重"}
                )),
    execute: async (interaction) => {
        const location = interaction.options.getString("location");
        const locationCode = locationMap[location];

        try {
            const weatherData = await getWeather(locationCode);
            if (weatherData) {
                const embed = {
                    title: `${location}の天気予報`,
                    color: 0x0099FF,
                    fields: weatherData.map(data => ({
                        name: data.time,
                        value: `${data.area_name}の天気: ${data.weather}`,
                        inline: false
                    }))
                };
                await interaction.reply({embeds: [embed]});
            } else {
                await interaction.reply("天気情報を取得できませんでした。");
            }
        } catch (error) {
            console.error(error);
            await interaction.reply("エラーが発生しました。");
        }
    }
};

async function getWeather(locationCode) {
    try {
        const response = await axios.get(`${url}${locationCode}${json}`);
        const jmaJson = response.data;
        const weatherData = [];
        const timeSeries = jmaJson[0].timeSeries[0];
        const timeDefines = timeSeries.timeDefines;
        const areas = timeSeries.areas;

        for (let day = 0; day < timeDefines.length; day++) {
            const timeDefine = timeDefines[day];
            const formattedTime = `${timeDefine}`;
            for (let areaNum = 0; areaNum < areas.length; areaNum++) {
                const areaData = areas[areaNum];
                const areaName = areaData.area.name;
                const weather = areaData.weathers[day];
                weatherData.push({
                    time: `${formattedTime.slice(0, 10)} ${formattedTime.slice(11, 16)}`,
                    area_name: areaName.replace(/　/g, ''),
                    weather: weather.replace(/　/g, '')
                });
            }
        }
        return weatherData;
    } catch (error) {
        console.error("Error fetching weather data:", error);
        return null;
    }
}

