<template>
  <div>
    <div class="container">
      <div>
        <video-player :options="videoOptions" />
      </div>
    </div>
  </div>
</template>

<script>
import VideoPlayer from '@/components/VideoPlayer.vue';
export default {
  name: 'ViewSomeVideo',
  components: {
    VideoPlayer
  },
  data() {
    return {
      videoOptions: {
        autoplay: true,
        controls: true,
        sources: [
          {
            src:
              '/media/video/video.mp4',
              type: 'video/mp4'
          }
        ]
      }
    };
  },
  methods: {},
  created: {}
};
</script>

<style lang="scss" scoped>
@import '../assets/css/video-js.css';
@import '../assets/css/view_some_video.css';
</style>
