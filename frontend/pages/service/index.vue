<template>
    <div>
        <ServiceCard text="service" imgservice="../_nuxt/assets/service/service.png" />
        <div class="xxxs:py-6 md:py-10">
            <div class="body-padding_margin">
                <div class="container">
                    <div class="space-y-2 pb-2">
                        <h1
                            class="text-center text-primary font-oswald font-bold xxxs:text-2xl sm:text-3xl md:text-4xl">
                            Etcare SACCO Services</h1>
                        <p class="text-center text-primary font-light font-oswald xxxs:text-base sm:text-lg lg:text-base">
                            Our services include Savings, Loans,
                            Micro Insurance, and the digital Equb system, all designed to meet your specific needs and
                            help you
                            achieve your financial goals.
                        </p>
                    </div>
                </div>
            </div>
        </div>

        <div class="xxxs:py-6 md:py-12">
            <div class="body-padding_margin">
                <div class="container">
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-0 service-body">
                        <div :class="{ 'onscreenleft': isVisibleleft1 }" class=" offscreenleft" ref="myElementleft1">
                            <img src="../../assets/service/saving.png" alt="Description" class="service-image" />
                        </div>
                        <div :class="{ 'onscreenright': isVisibleright1 }" class="offscreenright" ref="myElementright1">
                            <div class="space-y-4 p-4">
                                <h1 class="text-secondary font-oswald xxxs:text-3xl md:text-4xl font-bold">Saving</h1>
                                <p
                                    class="text-primary font-roboto text-xl text-justify xxxs:text-base sm:text-lg lg:text-xl">
                                    We
                                    understand the importance of saving
                                    for
                                    the future, which is why we offer convenient and flexible savings options to help
                                    our
                                    members
                                    build financial security. Whether it's short-term goals or long-term planning, our
                                    savings
                                    accounts provide a safe and reliable way to grow your money.</p>
                                <div class="flex">
                                    <nuxt-link
                                        class="service-button items-center text-xl font-oswald flex space-x-4 font-roboto"
                                        to="/service/saving">
                                        <svg xmlns="http://www.w3.org/2000/svg" width="2em" height="2em"
                                            viewBox="0 0 24 24">
                                            <path fill="currentColor"
                                                d="m7.45 17.45l-1.4-1.4L9.075 13H2v-2h7.075L6.05 7.95l1.4-1.4L12.9 12zM13 17v-2h9v2zm0-8V7h9v2zm3 4v-2h6v2z">
                                            </path>
                                        </svg>
                                        <span>Learn More</span>
                                    </nuxt-link>
                                </div>
                            </div>
                        </div>
                        <div :class="{ 'onscreenleft': isVisibleleft2 }" class="offscreenleft" ref="myElementleft2">
                            <div class="space-y-4 p-4">
                                <h1 class="text-secondary font-oswald xxxs:text-3xl md:text-4xl font-bold">Training</h1>
                                <p
                                    class="text-primary font-roboto text-xl text-justify xxxs:text-base sm:text-lg lg:text-xl">
                                    We
                                    understand the importance of saving
                                    for
                                    the future, which is why we offer convenient and flexible savings options to help
                                    our
                                    members
                                    build financial security. Whether it's short-term goals or long-term planning, our
                                    savings
                                    accounts provide a safe and reliable way to grow your money.</p>
                                <div class="flex">
                                    <nuxt-link
                                        class="service-button items-center text-xl font-oswald flex space-x-4 font-roboto"
                                        to="/service/training">
                                        <svg xmlns="http://www.w3.org/2000/svg" width="2em" height="2em"
                                            viewBox="0 0 24 24">
                                            <path fill="currentColor"
                                                d="m7.45 17.45l-1.4-1.4L9.075 13H2v-2h7.075L6.05 7.95l1.4-1.4L12.9 12zM13 17v-2h9v2zm0-8V7h9v2zm3 4v-2h6v2z">
                                            </path>
                                        </svg>
                                        <span>Learn More</span>
                                    </nuxt-link>
                                </div>
                            </div>
                        </div>
                        <div :class="{ 'onscreenright': isVisibleright2 }" class=" offscreenright"
                            ref="myElementright2">
                            <img src="../../assets/service/training.png" class="service-image" alt="saving" />
                        </div>
                        <div :class="{ 'onscreenleft': isVisibleleft3 }" class=" offscreenleft" ref="myElementleft3">
                            <img src="../../assets/service/equb.png" alt="saving" class="service-image" />
                        </div>
                        <div :class="{ 'onscreenright': isVisibleright3 }" class="offscreenright" ref="myElementright3">
                            <div class="space-y-4 p-4">
                                <h1 class="text-secondary font-oswald xxxs:text-3xl md:text-4xl font-bold">Equb</h1>
                                <p
                                    class="text-primary font-roboto text-xl text-justify xxxs:text-base sm:text-lg lg:text-xl">
                                    We
                                    understand the importance of saving
                                    for
                                    the future, which is why we offer convenient and flexible savings options to help
                                    our
                                    members
                                    build financial security. Whether it's short-term goals or long-term planning, our
                                    savings
                                    accounts provide a safe and reliable way to grow your money.</p>
                                <div class="flex">
                                    <nuxt-link
                                        class="service-button items-center text-xl font-oswald flex space-x-4 font-roboto"
                                        to="/service/equb">
                                        <svg xmlns="http://www.w3.org/2000/svg" width="2em" height="2em"
                                            viewBox="0 0 24 24">
                                            <path fill="currentColor"
                                                d="m7.45 17.45l-1.4-1.4L9.075 13H2v-2h7.075L6.05 7.95l1.4-1.4L12.9 12zM13 17v-2h9v2zm0-8V7h9v2zm3 4v-2h6v2z">
                                            </path>
                                        </svg>
                                        <span>Learn More</span>
                                    </nuxt-link>
                                </div>
                            </div>
                        </div>
                        <div :class="{ 'onscreenleft': isVisibleleft4 }" class="offscreenleft" ref="myElementleft4">
                            <div class="space-y-4 p-4">
                                <h1 class="text-secondary font-oswald xxxs:text-3xl md:text-4xl font-bold">loan</h1>
                                <p
                                    class="text-primary font-roboto text-xl text-justify xxxs:text-base sm:text-lg lg:text-xl">
                                    We
                                    understand the importance of saving
                                    for
                                    the future, which is why we offer convenient and flexible savings options to help
                                    our
                                    members
                                    build financial security. Whether it's short-term goals or long-term planning, our
                                    savings
                                    accounts provide a safe and reliable way to grow your money.</p>
                                <div class="flex">
                                    <nuxt-link
                                        class="service-button items-center text-xl font-oswald flex space-x-4 font-roboto"
                                        to="/service/loan">
                                        <svg xmlns="http://www.w3.org/2000/svg" width="2em" height="2em"
                                            viewBox="0 0 24 24">
                                            <path fill="currentColor"
                                                d="m7.45 17.45l-1.4-1.4L9.075 13H2v-2h7.075L6.05 7.95l1.4-1.4L12.9 12zM13 17v-2h9v2zm0-8V7h9v2zm3 4v-2h6v2z">
                                            </path>
                                        </svg>
                                        <span>Learn More</span>
                                    </nuxt-link>
                                </div>
                            </div>
                        </div>
                        <div :class="{ 'onscreenright': isVisibleright4 }" class=" offscreenright"
                            ref="myElementright4">
                            <img src="../../assets/service/loan.png" alt="saving" class="service-image" />
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            isVisibleleft1: false,
            isVisibleright1: false,
            isVisibleleft2: false,
            isVisibleright2: false,
            isVisibleleft3: false,
            isVisibleright3: false,
            isVisibleleft4: false,
            isVisibleright4: false,
        };
    },
    mounted() {
        window.addEventListener('scroll', this.handleScroll);
        this.handleScroll(); // Initial check
    },
    beforeDestroy() {
        window.removeEventListener('scroll', this.handleScroll);
    },
    methods: {
        handleScroll() {
            const imageContainerleft1 = this.$refs.myElementleft1;
            const imageContainerright1 = this.$refs.myElementright1;
            const imageContainerleft2 = this.$refs.myElementleft2;
            const imageContainerright2 = this.$refs.myElementright2;
            const imageContainerleft3 = this.$refs.myElementleft3;
            const imageContainerright3 = this.$refs.myElementright3;
            const imageContainerleft4 = this.$refs.myElementleft4;
            const imageContainerright4 = this.$refs.myElementright4;
            const rectleft1 = imageContainerleft1.getBoundingClientRect();
            const rectright1 = imageContainerright1.getBoundingClientRect();
            const rectleft2 = imageContainerleft2.getBoundingClientRect();
            const rectright2 = imageContainerright2.getBoundingClientRect();
            const rectleft3 = imageContainerleft3.getBoundingClientRect();
            const rectright3 = imageContainerright3.getBoundingClientRect();
            const rectleft4 = imageContainerleft4.getBoundingClientRect();
            const rectright4 = imageContainerright4.getBoundingClientRect();
            this.isVisibleleft1 =
                rectleft1.top >= 0 && rectleft1.top <= window.innerHeight - 100 ||
                rectleft1.bottom >= 100 && rectleft1.bottom <= window.innerHeight;
            this.isVisibleright1 =
                rectright1.top >= 0 && rectright1.top <= window.innerHeight - 100 ||
                rectright1.bottom >= 100 && rectright1.bottom <= window.innerHeight;
            this.isVisibleleft2 =
                rectleft2.top >= 0 && rectleft2.top <= window.innerHeight - 100 ||
                rectleft2.bottom >= 100 && rectleft2.bottom <= window.innerHeight;
            this.isVisibleright2 =
                rectright2.top >= 0 && rectright2.top <= window.innerHeight - 100 ||
                rectright2.bottom >= 100 && rectright2.bottom <= window.innerHeight;
            this.isVisibleleft3 =
                rectleft3.top >= 0 && rectleft3.top <= window.innerHeight - 100 ||
                rectleft3.bottom >= 100 && rectleft3.bottom <= window.innerHeight;
            this.isVisibleright3 =
                rectright3.top >= 0 && rectright3.top <= window.innerHeight - 100 ||
                rectright3.bottom >= 100 && rectright3.bottom <= window.innerHeight;
            this.isVisibleleft4 =
                rectleft4.top >= 0 && rectleft4.top <= window.innerHeight - 100 ||
                rectleft4.bottom >= 100 && rectleft4.bottom <= window.innerHeight;
            this.isVisibleright4 =
                rectright4.top >= 0 && rectright4.top <= window.innerHeight - 100 ||
                rectright4.bottom >= 100 && rectright4.bottom <= window.innerHeight;
        }
    }
};
</script>

<style>
.offscreenleft {
    opacity: 0;
    transform: translateX(-100%);
    /* Adjust as needed */
    transition: opacity 1s ease-in-out, transform 1.5s ease-in-out;
}

.onscreenleft {
    opacity: 1;
    transform: translateX(0);
    transition: opacity 1s ease-in-out, transform 1s ease-in-out;
}

.offscreenright {
    opacity: 0;
    transform: translateX(100%);
    /* Adjust as needed */
    transition: opacity 1s ease-in-out, transform 1s ease-in-out;
}

.onscreenright {
    opacity: 1;
    transform: translateX(0);
    transition: opacity 1s ease-in-out, transform 1s ease-in-out;
}

.box-image {
    transform: translateX(0);
    overflow-x: hidden;
}

.cover-service-img {
    background-image: url('../assets/2.jpg');
    height: 33rem;
    display: flex;
    align-items: center;
    background-size: cover;
    background-position: center;
}

.service-body {
    overflow: hidden;
}

.service-button {
    background-color: theme('colors.primary');
    color: theme('colors.background');
    padding: 0.5rem 2rem;
    border-radius: 0.25rem;
    transition: all 1s ease;
}

.service-button:hover {
    color: theme('colors.secondary');
    background-color: theme('colors.white');
    border: solid 1px theme('colors.secondary');
}

.service-image {
    width: 100%;
    height: 100%;
}
</style>