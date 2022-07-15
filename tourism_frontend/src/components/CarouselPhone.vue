<template>
  <Carousel>
    <template #slides="{ slidesCount }" >
      <Slide v-for="(imagePhone, index) in imagesPhone" :key="imagePhone.id">
        <img :src="imagePhone.url" />
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

import "vue3-carousel/dist/carouselphone.css";

export default defineComponent({
  name: "Basic",
  props: {
    imagesPhone: Array,
  },
  components: {
    Carousel,
    Slide,
    Pagination,
    Navigation,
  },

  setup(props, { emit }) {
    const { imagesPhone } = toRefs(props);

    const deleteImage = (index) => emit("delete-image", index);

    return { imagesPhone, deleteImage };
  },
});
</script>
