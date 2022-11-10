<template>
  <div class="home">
    <h1>home</h1>
    <button v-on:click="test">api 테스트</button>
    <youtube
      v-bind:video-id="videoId"
      v-bind:player-vars="playerVars"
      ref="youtube"
    />
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      videoId: "CgKUIHw2lHc",
      playerVars: {
        controls: 1,
        autoplay: 1,
      },
    };
  },
  methods: {
    async test() {
      const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY;
      const API_URL = process.env.VUE_APP_YOUTUBE_API_URL;
      try {
        const response = await axios.get(API_URL, {
          params: {
            key: API_KEY,
            type: "video",
            part: "snippet",
            q: "",
          },
        });
        console.log(response.data.items);
        console.log(response.data.items[0]);
        console.log(response.data.items[0].id.videoId);
        console.log(response.data.items[0].snippet.title);
        console.log(response.data.items[0].snippet.description);
        console.log(response.data.items[0].snippet.thumbnails.default.url);
        this.videoId = response.data.items[0].id.videoId
      } catch (error) {
        console.log(error);
      }
    },
  },
};
</script>