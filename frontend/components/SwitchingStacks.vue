<template>
  <div class="carousel relative w-full h-auto">
    
    <img 
      :src="images[currentImageIndex]" 
      :key="currentImageIndex" 
      :class="{'visible': isVisible}" 
      class="w-full h-auto object-cover transition-all duration-1000 ease-in-out" 
      alt="home page image" 
    />

    <svg class="overlay-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100%" height="100%">
      <circle cx="-30" cy="10" r="50" fill="url(#grad1)" />
      <circle cx="20" cy="0" r="20" fill="url(#grad2)" />
      <circle cx="140" cy="90" r="50" fill="url(#grad1)" />
      <circle cx="90" cy="100" r="20" fill="url(#grad2)" />
      <linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%" style="stop-color:#214080;stop-opacity:1" />
        <stop offset="100%" style="stop-color:#D92A27;stop-opacity:1" />
      </linearGradient>
      <linearGradient id="grad2" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%" style="stop-color:#214080;stop-opacity:1" />
        <stop offset="100%" style="stop-color:#D92A27;stop-opacity:1" />
      </linearGradient>
    </svg>

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
                    {{ title[currentImageIndex] }}</h1>
                </div>
                <div>
                  <nuxt-link :to="link[currentImageIndex]"
                    class="xxxs:text-xs xs:text-sm sm:text-base md:text-lg xxl:text-xl etcare-button px-6 py-1 md:px-10 xxl:px-14 md:py-1 xxl:py-2 items-center font-oswald">
                    Read More
                  </nuxt-link>
                </div>
              </div>
            </div>

            <button @click="nextImage"> <svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1.5em"
                viewBox="0 0 24 24">
                <path fill="currentColor"
                  d="M15.835 11.63L9.205 5.2C8.79 4.799 8 5.042 8 5.57v12.86c0 .528.79.771 1.205.37l6.63-6.43a.5.5 0 0 0 0-.74">
                </path>
              </svg>
            </button>
          </div>

          <div class="home-links flex font-oswald">
            <nuxt-link class="link-home"
              :class="{ 'xxxs:border-t-2 md:border-t-4 border-primary': 0 === currentImageIndex }"
              to="/service/saving">Saving Service</nuxt-link>
            <nuxt-link class="link-home"
              :class="{ 'xxxs:border-t-2 md:border-t-4 border-primary': 1 === currentImageIndex }"
              to="/service/training">Training Service</nuxt-link>
            <nuxt-link class="link-home"
              :class="{ 'xxxs:border-t-2 md:border-t-4 border-primary': 2 === currentImageIndex }"
              to="/service/equb">Equb
              Service</nuxt-link>
            <nuxt-link class="link-home"
              :class="{ 'xxxs:border-t-2 md:border-t-4 border-primary': 3 === currentImageIndex }"
              to="/service/loan">Loan
              Service</nuxt-link>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { NuxtImg } from '#components';

export default {
  data() {
    return {
      images: [
        '../_nuxt/assets/homepage1.png',
        '../_nuxt/assets/Untitled-3.png',
        '../_nuxt/assets/Untitled-2.png',
        '../_nuxt/assets/Untitled-1.png',
      ],
      title: [
        "Secure Your Financial Future with Our Trustworthy Saving Solutions – Building Wealth with Confidence.",
        "Empower Your Future with Skill-Building Training Programs Designed to Elevate Your Financial Independence.",
        "Join a Community of Collective Savings with Equb – Build Wealth Together for a Brighter Future!",
        "Achieve Your Ambitions with Our Flexible Loan Options – Empowering You to Take the Next Step!",
      ],
      link: [
        "/service/saving",
        "/service/training",
        "/service/equb",
        "/service/loan",
      ],
      currentImageIndex: 0,
      isVisible: true,
    };
  },
  methods: {
    nextImage() {
      this.isVisible = false;
      setTimeout(() => {
        this.currentImageIndex = (this.currentImageIndex + 1) % this.images.length;
        this.isVisible = true;
      }, 1000); // Match this duration with your CSS transition duration
    },
    prevImage() {
      setTimeout(() => {
        this.currentImageIndex =
        (this.currentImageIndex - 1 + this.images.length) % this.images.length;
      }, 1000);
    },
  },
  mounted() {
    this.interval = setInterval(this.nextImage, 7000);
  },
  beforeDestroy() {
    clearInterval(this.interval);
  },
};
</script>

<style scoped>

img {
  opacity: 0;
  transition: opacity 1s ease-in-out;
}

img.visible {
  opacity: 1;
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
  }

  .link-home:hover {
    border-top: solid 2px theme('colors.primary');
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

  .link-home:hover {
    border-top: solid 2px theme('colors.primary');
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
  }

  .link-home:hover {
    border-top: solid 3px theme('colors.primary');
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
  }

  .link-home:hover {
    border-top: solid 4px theme('colors.primary');
  }
}

@media (min-width: 1448px) {
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
  }

  .link-home:hover {
    border-top: solid 4px theme('colors.primary');
  }
}
</style>