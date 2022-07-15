<template>
  <carousel>
    <Slide v-for="(image, index) in images" :key="image.id">
        <img :src="image.url" />
    </Slide>

    <template #addons>
      <navigation />
      <pagination />
    </template>
  </carousel>
</template>

<script lang="ts">
// If you are using PurgeCSS, make sure to whitelist the carousel CSS classes
import 'vue3-carousel/dist/carouselphone.css';
import { defineComponent, ref } from "vue";
import { Carousel, Slide, Pagination, Navigation } from 'vue3-carousel';

export default defineComponent({
  name: 'AppPhone',
  components: {
    Carousel,
    Slide,
    Pagination,
    Navigation,
  },
  setup() {
    const _images = [
      { id: 1, url: "https://images.hdqwalls.com/download/sunset-over-rocky-ocean-4k-320x568.jpg" },
      { id: 2, url: "https://static2.tap-trip.com/uploads/production/timeline_thread_photo/image/39416236/c5ae4fa1-c485-49fa-b89b-b089a1aa44bc.jpg" },
      { id: 3, url: "https://images.hdqwalls.com/download/ocean-waves-at-sunset-320x568.jpg" },
      { id: 4, url: "https://images.hdqwalls.com/download/tree-in-center-of-lake-reflection-in-water-ye-320x568.jpg" },
      { id: 5, url: "https://images.hdqwalls.com/download/mount-rainier-5k-29-320x568.jpg" },
      { id: 6, url: "https://i.pinimg.com/736x/10/5c/c1/105cc109d57406484adcbb14f615e910--canada-travel-moraine-lake.jpg" },
      { id: 7, url: "https://i.pinimg.com/474x/5b/76/e8/5b76e8992a8d022e396a8d4560391f91--norway-travel-bergen.jpg" },
      { id: 8, url: "https://images.hdqwalls.com/download/perfect-seashore-new-320x568.jpg" },
      { id: 9, url: "https://images.hdqwalls.com/download/mountains-5k-retina-8u-320x568.jpg" },
      { id: 10, url: "https://sun9-79.userapi.com/impg/pFyEYcXMMZy-a9z2SlA9DuSQfW6o9sJ3Nqo2kw/5RKutmM7z2o.jpg?size=320x568&quality=96&sign=96388d454db1bb8035c69a05c8f0dd75&c_uniq_tag=WZnjN1BzGwVANGkeQXVqHZ-issnoGpALrleKl4RQEkU&type=album" },
    ];
    const images = ref(_images);
    const handelDeleteImage = (index: number) => images.value.splice(index, 1);

    return { handelDeleteImage, images };
  },
});
</script>