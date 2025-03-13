<template>
  <div class="slideshow-container carousel relative w-full">
    <div v-for="(slide, index) in slides" :key="index" class="image-sliderfade fade"
      :style="{ display: currentSlide === index ? 'block' : 'none' }">
      <img :src="slide.src" style="width: 100%" />
    </div>

    <div class="overlay-svg">
      <SvgComp />
    </div>

    <div class="carousel-body">
      <div class="body-padding_margin">
        <div class="container lg:gap-20 xl:gap-32">
          <div class="carousel-content flex justify-center items-center text-center gap-6">
            <button @click="prevImage">
              <svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1.5em" viewBox="0 0 24 24">
                <path fill="currentColor"
                  d="m8.165 11.63l6.63-6.43C15.21 4.799 16 5.042 16 5.57v12.86c0 .528-.79.771-1.205.37l-6.63-6.43a.5.5 0 0 1 0-.74">
                </path>
              </svg>
            </button>

            <div class="flex flex-col items-center">
              <div class="homecontent space-y-6">
                <div>
                  <h1
                    class="text-primary xxxs:text-lg xs:text-xl sm:text-3xl md:text-4xl xxl:text-5xl text-f font-oswald xxxs:py-4 lg:py-8">
                    {{ title[currentSlide] }}
                  </h1>
                </div>

                <div class="flex justify-center item-center">
                  <nuxt-link :to="link[currentSlide]"
                    class="etcare-button xxxs:text-xs xs:text-sm sm:text-base md:text-lg xxl:text-xl px-6 py-1 md:px-10 xxl:px-14 md:py-1 xxl:py-2 items-center font-oswald">
                    Read More
                  </nuxt-link>
                </div>
              </div>
            </div>

            <button @click="nextImage">
              <svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1.5em" viewBox="0 0 24 24">
                <path fill="currentColor"
                  d="M15.835 11.63L9.205 5.2C8.79 4.799 8 5.042 8 5.57v12.86c0 .528.79.771 1.205.37l6.63-6.43a.5.5 0 0 0 0-.74">
                </path>
              </svg>
            </button>
          </div>

          <div class="home-links flex font-oswald">
            <nuxt-link class="link-home" :class="{ 'link-home-not': 0 === currentSlide }" to="/service/saving">Saving
              Service</nuxt-link>
            <nuxt-link class="link-home" :class="{ 'link-home-not': 1 === currentSlide }" to="/service/loan">Loan
              Service</nuxt-link>
            <nuxt-link class="link-home" :class="{ 'link-home-not': 2 === currentSlide }" to="/service/equb">Equb
              Service</nuxt-link>
            <nuxt-link class="link-home" :class="{ 'link-home-not': 3 === currentSlide }"
              to="/service/training">Training Service</nuxt-link>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import SvgComp from './SvgComp.vue';

const slides = ref([
  { src: '/homepage1.jpeg', caption: 'Image caption 1' },
  { src: '/homepage2.jpeg', caption: 'Image caption 2' },
  { src: '/homepage3.jpeg', caption: 'Image caption 3' },
  { src: '/homepage4.jpeg', caption: 'Image caption 4' },
]);

const title = ref([
  'Secure Your Financial Future with Our Trustworthy Saving Solutions – Building Wealth with Confidence.',
  'Achieve Your Ambitions with Our Flexible Loan Options – Empowering You to Take the Next Step!',
  'Join a Community of Collective Savings with Equb – Build Wealth Together for a Brighter Future!',
  'Empower Your Future with Skill-Building Training Programs Designed to Elevate Your Financial Independence.',
]);

const link = ref(['/service/saving', '/service/loan', '/service/equb', '/service/training']);

const currentSlide = ref(0);

const startSlideshow = () => {
  setInterval(() => {
    currentSlide.value++;
    if (currentSlide.value >= slides.value.length) {
      currentSlide.value = 0;
    }
  }, 30000);
};

const nextImage = () => {
  currentSlide.value = (currentSlide.value + 1) % slides.value.length;
};

const prevImage = () => {
  currentSlide.value =
    (currentSlide.value - 1 + slides.value.length) % slides.value.length;
};

onMounted(() => {
  startSlideshow();
});
</script>

<style scoped>
* {
  box-sizing: border-box;
}

.image-sliderfade {
  display: none;
}

img {
  vertical-align: middle;
}

.slideshow-container {
  max-width: 100%;
  position: relative;
  margin: auto;
}

.fade {
  -webkit-animation-name: fade-image;
  -webkit-animation-duration: 1.5s;
  animation-name: fade-image;
  animation-duration: 1.5s;
}

@-webkit-keyframes fade-image {
  from {
    opacity: 0.8;
  }

  to {
    opacity: 1;
  }
}

@keyframes fade-image {
  from {
    opacity: 0.8;
  }

  to {
    opacity: 1;
  }
}

@media (min-width: 0) {
  .overlay-svg {
    display: none;
  }

  .carousel-body button {
    display: none;
  }

  .home-links {
    justify-content: space-between;
    padding-top: 2rem;
    padding-bottom: 3.5rem;
    color: theme('colors.secondary');
    font-weight: bolder;
    font-size: theme('fontSize.xxs');
    width: 100%;
    border-top: 0px solid theme('colors.primary');
    transition: border-top 0.5s ease-in-out;
  }
}

@media (min-width: 400px) {
  .overlay-svg {
    display: none;
  }

  .carousel-body button {
    display: none;
  }

  .home-links {
    justify-content: space-between;
    padding-top: 2.5rem;
    padding-bottom: 3.5rem;
    color: theme('colors.secondary');
    font-weight: bolder;
    font-size: theme('fontSize.xs');
    width: 100%;
  }
}

@media (min-width: 768px) {
  .overlay-svg {
    display: none;
  }

  .carousel-body button {
    display: none;
  }

  .carousel-body {
    position: relative;
  }

  .home-links {
    justify-content: space-between;
    padding-top: 4.5rem;
    padding-bottom: 5.5rem;
    color: theme('colors.secondary');
    font-weight: bolder;
    font-size: theme('fontSize.base');
    width: 100%;
    border-top: 0px solid transparent;
    transition: border-top-color 0.3s ease-in-out, border-top-width 0.3s ease-in-out;
  }
}

@media (min-width: 1024px) {
  .carousel-body {
    position: absolute;
    z-index: 4;
    top: 60%;
    left: 50%;
    transform: translate(-50%, -50%);
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    width: 100%;
    height: 100%;
  }

  .overlay-svg {
    display: inline-block;
  }

  .imagewithsvg {
    position: relative;
  }

  .overlay-svg {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    opacity: 0.65;
    pointer-events: none;
  }

  .carousel button {
    display: block;
    color: theme('colors.primary');
    padding: 0.5rem 0.9rem;
    background-color: rgba(255, 255, 255, 0.5);
    border-radius: 6px;
    font-size: 1.2rem;
    transition: all 0.4s ease-in-out;
    cursor: pointer;
  }


  .carousel button:hover {
    background: theme('colors.white');
  }

  .home-links {
    justify-content: space-between;
    padding-top: 4.5rem;
    padding-bottom: 5.5rem;
    color: theme('colors.secondary');
    font-weight: bolder;
    font-size: theme('fontSize.lg');
    width: 100%;
    border-top: 0px solid transparent;
    transition: border-top-color 0.3s ease, border-top-width 0.3s ease;
  }
}

@media (min-width: 1448px) {
  .carousel-img {
    opacity: 0;
    transition: opacity 1s ease-in-out;
  }

  .carousel-img.visible {
    opacity: 1;
  }

  .carousel-body {
    position: absolute;
    z-index: 4;
    top: 60%;
    left: 50%;
    transform: translate(-50%, -50%);
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    width: 100%;
    height: 100%;
  }

  .imagewithsvg {
    position: relative;
  }

  .overlay-svg {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    opacity: 0.65;
    pointer-events: none;
  }

  .carousel button {
    color: theme('colors.primary');
    padding: 0.5rem 0.9rem;
    background-color: rgba(255, 255, 255, 0.5);
    border-radius: 6px;
    font-size: 1.2rem;
    cursor: pointer;
    transition: all 0.4s ease-in-out;
  }

  .carousel button:hover {
    background: theme('colors.white');
  }

  .home-links {
    justify-content: space-between;
    padding-top: 4.5rem;
    padding-bottom: 5.5rem;
    color: theme('colors.secondary');
    font-weight: bolder;
    font-size: theme('fontSize.xl');
    width: 100%;
    border-top: 0px solid transparent;
    transition: border-top-color 0.3s ease, border-top-width 0.3s ease;
  }
}

.link-home {
  position: relative;
}

.link-home::after {
  content: "";
  position: absolute;
  width: 0;
  height: 4px;
  top: -5px;
  left: 0;
  background: theme('colors.primary');
  transition: all 0.5s ease-in-out;
}

.link-home:hover::after {
  width: 100%;
}

.link-home-not::after {
  content: "";
  position: absolute;
  width: 0;
  height: 4px;
  top: -5px;
  left: 0;
  background: theme('colors.primary');
  transition: all 0.5s ease-in-out;
}

.link-home-not::after {
  width: 100%;
}

.link-home::after {
  transition: all 0.5s ease-in-out 0.1s;
}

.link-home:hover::after {
  transition-delay: 0s;
}
</style>