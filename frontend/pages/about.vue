<template>
    <div>
        <ServiceCard text="About" imgservice="../_nuxt/assets/service/about.png" />

        <div class="body-padding_margin">
            <div class="container">
                <div class="grid grid-cols-1 md:grid-cols-2 xxxs:gap-4 md:gap-8 about-border xxxs:p-6 md:p-12">
                    <div>
                        <img src="../assets/service/building.png" class="about-image" alt="building" />
                    </div>
                    <div class="xxxs:space-y-4 md:space-y-8">
                        <h1 class="text-primary font-bold text-justify xxxs:text-base md:text-lg">Etcare SACCOs Ltd is a
                            leading financial cooperative
                            dedicated to empowering individuals and
                            communities through innovative financial solutions.</h1>
                        <p class="text-primary text-justify xxxs:text-sm md:text-base">We are driven by the mission of
                            financial literacy and
                            inclusion, ensuring that every member has
                            access to the knowledge and resources needed to make sound financial decisions. Through
                            education
                            and transparent practices, we strive to uplift our members and foster long-term financial
                            stability.
                            and transparent practices, we strive to uplift our members and foster long-term financial
                            stability.
                            and transparent practices, we strive to uplift our members and foster long-term financial
                            stability.
                        </p>
                    </div>
                </div>

                <div class="pt-8 pb-8 xxxs:space-y-4 md:space-y-8">
                    <h1 class="text-secondary text-oswald font-bold xxxs:text-3xl md:text-4xl text-center">
                        About us</h1>
                    <div class="grid grid-cols-1 md:grid-cols-2 xxxs:gap-4 md:gap-8">
                        <div class="flex items-center">
                            <p class="text-primary font-robot text-justify xxxs:text-base md:text-lg">At Etcare SACCOs
                                Ltd, we're known for
                                our professionalism and dedication in finance. Our main
                                goal is to become the best savings and credit cooperative society by 2020, helping our
                                members
                                improve their lives. Using the latest technology, we offer a wide range of services like
                                savings, loans, and banking that fit everyone's needs. We always stick to honesty,
                                transparency,
                                and accountability in everything we do. Our mission is to teach people about money and
                                make
                                sure
                                everyone benefits from our services. Our values include loyalty, honesty, clear
                                communication,
                                responsibility, and helping others. We're committed to creating a strong financial
                                future
                                for
                                our members and our community.</p>
                        </div>
                        <div>
                            <img src="../assets/service/ETCA1490.png" class="about-image" alt="etc" />
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <div class="Our-Best-Quality">
            <div class="body-padding_margin  space-y-4">
                <div class="container">
                    <div class="grid  grid-cols-1 md:grid-cols-2 xxxs:gap-4 md:gap-8 ">
                        <div class="space-y-4">
                            <h1 class="text-secondary font-oswald font-bold  xxxs:text-3xl md:text-4xl pt-8">Our
                                Best Quality</h1>
                            <p class="text-primary font-robot text-justify xxxs:text-sm md:text-base">At Etcare SACCOs
                                Ltd, we
                                pride ourselves on
                                delivering exceptional quality in every aspect of
                                our
                                services. Our commitment to excellence is driven by a deep understanding of our members'
                                needs
                                and a desire to exceed their expectations.</p>
                        </div>
                        <div class="flex items-center justify-center">
                            <img src="../assets/logo1-removebg.png" class="w-32 h-32" alt="logo" />

                        </div>
                    </div>

                    <div class="flex justify-center pt-5 pb-8">
                        <nuxt-link to="/contact"
                            class="xs:pt-1 xs:pb-1 xs:pl-5 xs:pr-5 md:pt-2 md:pb-2 md:pl-8 md:pr-8 about-button flex items-center space-x-4">
                            <svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" viewBox="0 0 20 20">
                                <path fill="currentColor"
                                    d="M17 11v3l-3-3H8a2 2 0 0 1-2-2V2c0-1.1.9-2 2-2h10a2 2 0 0 1 2 2v7a2 2 0 0 1-2 2zm-3 2v2a2 2 0 0 1-2 2H6l-3 3v-3H2a2 2 0 0 1-2-2V8c0-1.1.9-2 2-2h2v3a4 4 0 0 0 4 4z">
                                </path>
                            </svg>
                            <h1> contact us</h1>
                        </nuxt-link>
                    </div>
                </div>
            </div>
        </div>

        <div class=" pt-16 pb-32">
            <div class="body-padding_margin space-y-2">
                <div class="container">
                    <h1 class="text-primary font-bold font-oswald text-center  xxxs:text-3xl md:text-4xl">
                        OUR
                        TEAM</h1>
                    <p class="text-primary xxxs:text-sm md:text-base font-robot text-center">The Hardworking Team behind
                        Etcare SACCO</p>

                    <div class="flex justify-between items-center xxxs:gap-2 md:gap-4 team-staff">
                        <div class="text-secondary arrow-back" @click="prevTeam"
                            :class="{ 'opacity-50 pointer-events-none': startIndex === 0 }">
                            <svg xmlns="http://www.w3.org/2000/svg" width="2.5em" height="2.5em" viewBox="0 0 24 24">
                                <path fill="currentColor"
                                    d="M11.8 13H15q.425 0 .713-.288T16 12t-.288-.712T15 11h-3.2l.9-.9q.275-.275.275-.7t-.275-.7t-.7-.275t-.7.275l-2.6 2.6q-.3.3-.3.7t.3.7l2.6 2.6q.275.275.7.275t.7-.275t.275-.7t-.275-.7zm.2 9q-2.075 0-3.9-.788t-3.175-2.137T2.788 15.9T2 12t.788-3.9t2.137-3.175T8.1 2.788T12 2t3.9.788t3.175 2.137T21.213 8.1T22 12t-.788 3.9t-2.137 3.175t-3.175 2.138T12 22">
                                </path>
                            </svg>
                        </div>

                        <team v-for="(member, index) in visibleTeamMembers" :key="index" :member="member" />

                        <div class="text-secondary arrow-forward" @click="nextTeam"
                            :class="{ 'opacity-50 pointer-events-none': endIndex >= teamMembers.length }">
                            <svg xmlns="http://www.w3.org/2000/svg" width="2.5em" height="2.5em" viewBox="0 0 24 24">
                                <path fill="currentColor"
                                    d="m12 16l4-4l-4-4l-1.4 1.4l1.6 1.6H8v2h4.2l-1.6 1.6zm0 6q-2.075 0-3.9-.788t-3.175-2.137T2.788 15.9T2 12t.788-3.9t2.137-3.175T8.1 2.788T12 2t3.9.788t3.175 2.137T21.213 8.1T22 12t-.788 3.9t-2.137 3.175t-3.175 2.138T12 22">
                                </path>
                            </svg>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue';

const teamMembers = ref([
    { name: 'Hnana', role: 'Role 1' },
    { name: 'Redu', role: 'Role 2' },
    { name: 'Samri', role: 'Role 3' },
    { name: 'Meseret', role: 'Role 4' },
    { name: 'Kidest', role: 'Role 5' },
    { name: 'Andualem', role: 'Role 6' },
    // Add more team members as needed
]);

const startIndex = ref(0);
const teamDisplayLimit = ref(1);

function updateTeamDisplayLimit() {
    const width = window.innerWidth;

    if (width >= 1024) { // lg breakpoint
        teamDisplayLimit.value = 4;
    } else if (width >= 768) { // md breakpoint
        teamDisplayLimit.value = 3;
    } else if (width >= 640) { // sm breakpoint
        teamDisplayLimit.value = 2;
    } else {
        teamDisplayLimit.value = 1;
    }
}

onMounted(() => {
    updateTeamDisplayLimit();
    window.addEventListener('resize', updateTeamDisplayLimit);
});

onBeforeUnmount(() => {
    window.removeEventListener('resize', updateTeamDisplayLimit);
});

const endIndex = computed(() => startIndex.value + teamDisplayLimit.value);
const visibleTeamMembers = computed(() => teamMembers.value.slice(startIndex.value, endIndex.value));

function nextTeam() {
    if (endIndex.value < teamMembers.value.length) {
        startIndex.value += 1;
    }
}

function prevTeam() {
    if (startIndex.value > 0) {
        startIndex.value -= 1;
    }
}
</script>

<style>
.arrow-forward,
.arrow-back {
    cursor: pointer;
    transition: opacity 0.3s ease;
}

.arrow-forward.opacity-50,
.arrow-back.opacity-50 {
    opacity: 0.5;
    pointer-events: none;
    /* Disable click */
}

.Our-Best-Quality {
    background-color: #FFDFDF;
}

.about-button {
    background-color: theme('colors.secondary');
    border-radius: 8px 8px 8px 0;
    padding: 0.7rem 3.5rem;
    transition: all 0.5s ease;
}

.about-button:hover {
    color: theme('colors.white');
    background-color: theme('colors.primary');

}

.about-border {
    border: 2px solid theme('colors.secondary');
    border-radius: 20px;
}

.about-image {
    width: 100%;
    height: 100%;
}
</style>