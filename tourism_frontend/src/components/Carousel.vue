<template>
  <Carousel>
    <template #slides="{ slidesCount }" >
      <Slide v-for="(image, index) in images" :key="image.id">
        <img :src="image.url" />
      </Slide>
    </template>

    <template #addons>
      <Navigation />
    </template>
  </Carousel>
</template>

<script>
import { defineComponent, registerRuntimeCompiler, toRefs } from "vue";
import { Carousel, Pagination, Navigation, Slide } from "vue3-carousel";

import "vue3-carousel/dist/carousel.css";

export default defineComponent({
  name: "Basic1",
  props: {
    images: Array,
  },
  components: {
    Carousel,
    Slide,
    Pagination,
    Navigation,
  },

  setup(props, { emit }) {
    const { images } = toRefs(props);

    const deleteImage = (index) => emit("delete-image", index);

    return { images, deleteImage };
  },
});
</script>
