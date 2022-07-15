<template>
  <Carousel :images="images" @deleteImage="handelDeleteImage" />
</template>

<script lang="ts">
import { defineComponent, ref } from "vue";
import Carousel from "./Carousel.vue";

export default defineComponent({
  components: {
    Carousel,
  },
  setup() {
    const _images = [
      { id: 1, url: "https://cdn.fishki.net/upload/post/201512/14/1775583/tn/1_03.jpg" },
      { id: 2, url: "https://cdn.fishki.net/upload/post/2017/06/27/2323519/tn/1-0-1c30d9-4f645798-orig.jpg" },
      { id: 3, url: "https://cdn.fishki.net/upload/post/2016/06/29/1997845/tn/7-11.jpg" },
      { id: 4, url: "https://cdn.fishki.net/upload/post/201603/24/1895688/tn/4_18.jpg" },
      { id: 5, url: "https://cdn.fishki.net/upload/post/2017/07/22/2342522/tn/kk.jpg" },
      { id: 6, url: "https://cdn.fishki.net/upload/post/2016/10/11/2102353/5569745d85333a4c8a1feab8cb9ed58e.jpg" },
      { id: 7, url: "https://cdn.fishki.net/upload/post/2019/08/19/3061999/tn/01386876fddc49d039c13996bf2fa826.jpg" },
      { id: 8, url: "https://www.красноармейскийрайон.рф/upload/000/u3/004/fbcf1eea.jpg" },
      { id: 9, url: "https://kirovpravda.ru/wp-content/uploads/2021/04/oleni.jpg" },
      { id: 10, url: "https://cdn.fishki.net/upload/post/2017/04/28/2278621/tn/d8a3c33619d875e51d67110ecc61265e.jpg" },
    ];
    const images = ref(_images);
    const handelDeleteImage = (index: number) => images.value.splice(index, 1);

    return { handelDeleteImage, images };
  },
});
</script>