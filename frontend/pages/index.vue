<template>
    <div class="etcare-home">
        <SwitchingStacks />

        <div class="bg-primary xxxs:py-4 md:py-8 xxl:py-12">
            <div class="body-padding_margin">
                <div class="container xxxs:space-y-4 md:space-y-6">
                    <h1 class="text-center font-oswald xxxs:text-3xl xxl:text-4xl font-bold text-background">
                        Who we are</h1>
                    <p class="text-center font-roboto xxxs:text-1xl sm:text-2xl">Etcare SACCO is a
                        member-driven
                        savings and credit cooperative dedicated to empowering individuals
                        through financial inclusion. We provide innovative financial services, from savings and loans to
                        investment opportunities, designed to meet the diverse needs of our members. Our commitment is
                        rooted in fostering financial literacy, economic stability, and sustainable growth for all
                        members
                        of the
                        cooperative. By prioritizing collaboration and leveraging modern technology, we aim to create a
                        community where every member can achieve financial independence and security.</p>
                    <div class="justify-center flex">
                        <nuxt-link
                            class="who-we-are-button items-center xxxs:text-lg md:text-lg xxl:text-xl font-oswald xxxs:space-x-2 md:space-x-4 flex font-roboto"
                            to="/about">
                            <svg xmlns="http://www.w3.org/2000/svg" width="2em" height="2em" viewBox="0 0 24 24">
                                <path fill="currentColor"
                                    d="m7.45 17.45l-1.4-1.4L9.075 13H2v-2h7.075L6.05 7.95l1.4-1.4L12.9 12zM13 17v-2h9v2zm0-8V7h9v2zm3 4v-2h6v2z">
                                </path>
                            </svg>
                            <span>Learn More</span>
                        </nuxt-link>
                    </div>
                </div>
            </div>
        </div>

        <div class=" xxxs:py-4 md:py-8">
            <div class="body-padding_margin">
                <div class="container">
                    <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
                        <div class="value-boje-section p-6 shadow-md space-y-4">
                            <div class="flex items-bottoms">
                                <img src="../assets/vision.png" class="h-16 w-16" alt="vision" />
                                <div class="cercle-nub">
                                    <h1 class="cercle-nub-on font-bold text-2xl">1</h1>
                                </div>
                            </div>
                            <h3 class="text-3xl font-bold">Vision</h3>
                            <p>To be Ethiopia's leading SACCO, empowering members with innovative financial solutions
                                and
                                fostering
                                community economic growth.</p>
                        </div>

                        <div class="value-boje-section p-6 shadow-md space-y-4">
                            <div class="flex items-bottoms">
                                <img src="../assets/Mission.png" class="h-16 w-16" alt="vision" />
                                <div class="cercle-nub">
                                    <h1 class="cercle-nub-on font-bold text-2xl">2</h1>
                                </div>
                            </div>
                            <h3 class="text-3xl font-bold">Mission</h3>
                            <p>We provide accessible, member-focused financial services, promoting savings, credit
                                access,
                                and
                                financial literacy to enhance members' financial well-being.</p>
                        </div>

                        <div class="value-boje-section p-6 shadow-md space-y-4">
                            <div class="flex items-bottoms">
                                <img src="../assets/object.png" class="h-16 w-16" alt="vision" />
                                <div class="cercle-nub">
                                    <h1 class="cercle-nub-on font-bold text-2xl">3</h1>
                                </div>
                            </div>
                            <h3 class="text-3xl font-bold">Objectives</h3>
                            <p>To support members' financial growth with tailored savings and loan products, while
                                promoting
                                financial education and sustainable practices for personal and community prosperity.</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <div class="photo-g text-center py-8">
            <h1 class="font-oswald xxxs:text-3xl md:text-4xl xl:text-5xl">Our Photo Gallery</h1>
        </div>

        <PhotoGallery />


        <div class="xxxs:py-4 md:py-8">
            <div class="body-padding_margin blog-letest">
                <div class="container xxxs:space-y-4 md:space-y-6">
                    <div class="flex justify-center pt-20">
                        <img src="../assets/logo1-removebg.png" alt="logo" />
                    </div>

                    <h1 class="text-center text-primary font-oswald xxxs:text-sm md:text-xl">Directly Blog Posts</h1>

                    <div class="flex justify-center pb-20">
                        <p
                            class="p-blog text-primary text-center font-oswald xxxs:text-xl xs:text-2xl sm:text-3xl md:text-4xl xl:text-5xl font-bold">
                            Latest News & Articles from
                            the Posts</p>
                    </div>

                    <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
                        <blog-component title="My First Blog Post"
                            summary="This is a blog post about my first experience with Nuxt.js."
                            image="../_nuxt/assets/dall1.png"
                            content="Lorem ipsum dolor sit amet, consectetur adipiscing elit..." author="John Doe"
                            publishedAt="2023-11-22" />
                        <blog-component title="My First Blog Post"
                            summary="This is a blog post about my first experience with Nuxt.js."
                            image="../_nuxt/assets/dall1.png"
                            content="Lorem ipsum dolor sit amet, consectetur adipiscing elit..." author="John Doe"
                            publishedAt="2023-11-22" />
                        <blog-component title="My First Blog Post"
                            summary="This is a blog post about my first experience with Nuxt.js."
                            image="../_nuxt/assets/dall1.png"
                            content="Lorem ipsum dolor sit amet, consectetur adipiscing elit..." author="John Doe"
                            publishedAt="2023-11-22" />
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
const refreshAccessToken = async () => {
    try {
        const response = await axios.post('http://127.0.0.1:8000/api/token/refresh/');
        return response.data.access_token;
    } catch (error) {
        console.error('Failed to refresh access token:', error);
        // Handle token renewal failure (e.g., log out the user)
    }
};


</script>

<style>
.etcare-home {
    overflow-x: hidden;
}

.blog-letest {
    background-image: url('../assets/services-bg.png');
    background-size: cover;
    background-position: center;
}

.p-blog {
    width: 60%;
}

.value-boje-section {
    position: relative;
    background-color: #FFCAC9;
    color: theme('colors.secondary');
    font-family: oswald, sans-serif;
    text-align: center;
    padding: 1.5rem 2.5rem;
    justify-content: center;
    border-radius: 8px;
    overflow: hidden;
    transition: color 1s ease;
    z-index: 1;
}

.value-boje-section:hover {
    color: #Fff;
}

.value-boje-section::before {
    content: '';
    width: 0%;
    position: absolute;
    display: block;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    height: 100%;
    border-radius: 8px;
    transition: width 1s ease;
    background: theme('colors.primary');
    z-index: -1;
}

.value-boje-section:hover::before {
    width: 100%;
}

@media (min-width: 200px) {
    .who-we-are-button {
        padding: 0.125rem 1.25rem;
        background-color: theme('colors.background');
        color: theme('colors.primary');
        border-radius: 5px;
        transition: color 1s, border 1s;
    }

    .who-we-are-button:hover {
        border: solid 2px theme('colors.secondary');
        color: theme('colors.secondary');
    }
}

@media (min-width: 500px) {
    .body-padding_margin {
        padding: 0 2.25rem;
    }
}

@media (min-width: 800px) {
    .body-padding_margin {
        padding: 0 3.5rem;
    }

    .who-we-are-button {
        padding: 0.35rem 2.25rem;
        background-color: theme('colors.background');
        color: theme('colors.primary');
        border-radius: 5px;
        transition: color 1s, border 1s;
    }

    .who-we-are-button:hover {
        border: solid 2px theme('colors.secondary');
        color: theme('colors.secondary');
    }
}

@media (min-width: 1200px) {
    .who-we-are-button {
        padding: 0.5rem 3rem;
        background-color: theme('colors.background');
        color: theme('colors.primary');
        border-radius: 5px;
        transition: color 1s, border 1s;
    }

    .who-we-are-button:hover {
        border: solid 2px theme('colors.secondary');
        color: theme('colors.secondary');
    }
}

.cercle-nub {
    width: 5rem;
    height: 5rem;
    border-radius: 2.5rem;
    color: #Fff;
    background-color: theme('colors.secondary');
    margin-left: -1rem;
}

.cercle-nub-on {
    width: 100%;
    height: 100%;
    justify-content: center;
    align-items: center;
    display: flex;
}

.items-bottoms {
    display: flex;
    align-items: end;
    justify-content: center;
}

.photo-g {
    background-image: url('../assets/photoG.png');
}
</style>