<template>
    <div class="web-body">
        <header :style="{ backgroundColor: headerBackgroundColor }" class="fixed top-0 left-0 right-0 z-10 text-primary
            body-padding_margin">
            <div class="container">
                <div class="flex items-center justify-between xs:h-20 md:h-24 xxl:h-32">
                    <div class="w-1/4">
                        <nuxt-link to="/"><img
                                class="xxxs:w-24 xxxs:h-10 sm:w-32 sm:h-12 md:w-32 md:h-16 xxl:w-34 xxl:h-20"
                                src="../assets/Etcare_logo1-removebg.png" alt="etcare logo" />
                        </nuxt-link>
                    </div>

                    <div class="w-2/4 hidden lg:inline ">
                        <div class="lg:text-sm flex justify-center items-center xxl:text-lg">
                            <div class="lg:space-x-6 xxl:space-x-8 flex item-center font-bold">
                                <nuxt-link to="/" class="links">HOME</nuxt-link>
                                <div class="flex items-center dropdown-link">
                                    <nuxt-link to="/service" class="links">SERVICE</nuxt-link>
                                    <svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" viewBox="0 0 24 24"
                                        class="ml-1">
                                        <path fill="currentColor" d="m5 8l7 8l7-8z"></path>
                                    </svg>
                                    <ul class="dropdown font-bold font-Roboto">
                                        <nuxt-link to="/service/saving">
                                            <li>
                                                Saving
                                            </li>
                                        </nuxt-link>
                                        <nuxt-link to="/service/equb">
                                            <li>
                                                equb
                                            </li>
                                        </nuxt-link>
                                        <nuxt-link to="/service/loan">
                                            <li>
                                                Loan
                                            </li>
                                        </nuxt-link>
                                        <nuxt-link to="/service/training">
                                            <li>
                                                training
                                            </li>
                                        </nuxt-link>
                                    </ul>
                                </div>
                                <nuxt-link to="/about" class="links">ABOUT</nuxt-link>
                                <nuxt-link to="/blog" class="links">BLOG</nuxt-link>
                                <nuxt-link to="/contact" class="links">CONTACT</nuxt-link>
                                <!-- <nuxt-link to="/MembershipForm" class="links">JOIN US</nuxt-link> -->
                            </div>
                        </div>
                    </div>

                    <div class="w-2/4 lg:hidden flex justify-center items-center">
                        <button @click="toggleMenu" aria-label="Toggle Menu">
                            <svg v-if="!isMenuOpen" xmlns="http://www.w3.org/2000/svg" width="2em" height="2em"
                                viewBox="0 0 24 24">
                                <path fill="currentColor"
                                    d="M4 18q-.425 0-.712-.288T3 17t.288-.712T4 16h16q.425 0 .713.288T21 17t-.288.713T20 18zm0-5q-.425 0-.712-.288T3 12t.288-.712T4 11h16q.425 0 .713.288T21 12t-.288.713T20 13zm0-5q-.425 0-.712-.288T3 7t.288-.712T4 6h16q.425 0 .713.288T21 7t-.288.713T20 8z">
                                </path>
                            </svg>

                            <svg v-if="isMenuOpen" xmlns="http://www.w3.org/2000/svg" width="2em" height="2em"
                                class="font-bold" viewBox="0 0 24 24">
                                <path fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round"
                                    stroke-width="1.5" d="m5 19l7-7m0 0l7-7m-7 7L5 5m7 7l7 7"></path>
                            </svg>
                        </button>
                    </div>

                    <div v-if="isMenuOpen"
                        class="absolute top-16 z-100 left-0 w-full bg-gray-100 lg:hidden shadow-lg z-10">
                        <ul class="space-y-4 items-center py-2 font-bold text-center">
                            <li class="border-b-2">
                                <nuxt-link to="/" @click="closeMenu">HOME</nuxt-link>
                            </li>
                            <li class="border-b-2 flex justify-center items-center">
                                <nuxt-link to="/service" @click="closeMenu">SERVICE</nuxt-link>
                                <svg @click="toggleMenuservice" xmlns="http://www.w3.org/2000/svg" width="1em"
                                    height="1em" viewBox="0 0 24 24" class="ml-1">
                                    <path fill="currentColor" d="m5 8l7 8l7-8z"></path>
                                </svg>
                                <div v-if="openMenuService"
                                    class="absolute top-16 z-100 left-0 w-full bg-gray-300 lg:hidden shadow-lg z-10">
                                    <ul class="space-y-4 py-2 font-bold text-center">
                                        <li @click="closeMenuservice" class="border-b-2">
                                            <nuxt-link to="/service/saving">
                                                Saving
                                            </nuxt-link>
                                        </li>
                                        <li @click="closeMenuservice" class="border-b-2">
                                            <nuxt-link to="/service/equb">
                                                equb
                                            </nuxt-link>
                                        </li>
                                        <li @click="closeMenuservice" class="border-b-2">
                                            <nuxt-link to="/service/loan">
                                                Loan
                                            </nuxt-link>
                                        </li>
                                        <li @click="closeMenuservice">
                                            <nuxt-link to="/service/training">
                                                training
                                            </nuxt-link>
                                        </li>
                                    </ul>
                                </div>

                            </li>
                            <li class="border-b-2">
                                <nuxt-link to="/about" @click="closeMenu">ABOUT</nuxt-link>
                            </li>
                            <li class="border-b-2">
                                <nuxt-link to="/blog" @click="closeMenu">BLOG</nuxt-link>
                            </li>
                            <li class="border-b-2">
                                <nuxt-link to="/contact" @click="closeMenu">CONTACT</nuxt-link>
                            </li>
                            <!-- <li>
                        <nuxt-link to="/MembershipForm" @click="closeMenu">JOIN US</nuxt-link>
                    </li> -->
                        </ul>
                    </div>

                    <div v-if="login" class="w-1/4 flex space-x-4 justify-end">
                        <nuxt-link to="/MembershipForm"
                            class="xxxs:text-xs md:text-sm xxl:text-base flex etcare-button xxxs:pt-1 xxxs:pb-1 xxxs:pl-2 xxxs:pr-2 md:pt-1 md:pb-1 md:pl-4 md:pr-4 xxl:pt-2 xxl:pb-2 xxl:pl-8 xxl:pr-8 space-x-10">
                            JOIN US
                        </nuxt-link>

                        <!-- <nuxt-link to="/login"
                    class="xxxs:text-xs md:text-sm xxl:text-base flex etcare-button xxxs:pt-1 xxxs:pb-1 xxxs:pl-2 xxxs:pr-2 md:pt-1 md:pb-1 md:pl-4 md:pr-4 xxl:pt-2 xxl:pb-2 xxl:pl-8 xxl:pr-8 space-x-10">
                    SIGN IN
                    <svg xmlns="http://www.w3.org/2000/svg" width="1.5em" height="1.5em" viewBox="0 0 24 24">
                        <path fill="currentColor"
                            d="M12 21v-2h7V5h-7V3h7q.825 0 1.413.588T21 5v14q0 .825-.587 1.413T19 21zm-2-4l-1.375-1.45l2.55-2.55H3v-2h8.175l-2.55-2.55L10 7l5 5z">
                        </path>
                    </svg>
                </nuxt-link> -->
                    </div>

                    <div class="w-1/4" v-else>
                        <div class="items-center flex space-x-2 user-profile hover:text-secondary"
                            @click="toggleUserProfile">
                            <svg xmlns="http://www.w3.org/2000/svg" width="2.5em" height="2.5em" viewBox="0 0 24 24">
                                <path fill="currentColor"
                                    d="M12 11q.825 0 1.413-.588Q14 9.825 14 9t-.587-1.413Q12.825 7 12 7q-.825 0-1.412.587Q10 8.175 10 9q0 .825.588 1.412Q11.175 11 12 11Zm0 2q-1.65 0-2.825-1.175Q8 10.65 8 9q0-1.65 1.175-2.825Q10.35 5 12 5q1.65 0 2.825 1.175Q16 7.35 16 9q0 1.65-1.175 2.825Q13.65 13 12 13Zm0 11q-2.475 0-4.662-.938q-2.188-.937-3.825-2.574Q1.875 18.85.938 16.663Q0 14.475 0 12t.938-4.663q.937-2.187 2.575-3.825Q5.15 1.875 7.338.938Q9.525 0 12 0t4.663.938q2.187.937 3.825 2.574q1.637 1.638 2.574 3.825Q24 9.525 24 12t-.938 4.663q-.937 2.187-2.574 3.825q-1.638 1.637-3.825 2.574Q14.475 24 12 24Zm0-2q1.8 0 3.375-.575T18.25 19.8q-.825-.925-2.425-1.612q-1.6-.688-3.825-.688t-3.825.688q-1.6.687-2.425 1.612q1.3 1.05 2.875 1.625T12 22Zm-7.7-3.6q1.2-1.3 3.225-2.1q2.025-.8 4.475-.8q2.45 0 4.463.8q2.012.8 3.212 2.1q1.1-1.325 1.713-2.95Q22 13.825 22 12q0-2.075-.788-3.887q-.787-1.813-2.15-3.175q-1.362-1.363-3.175-2.151Q14.075 2 12 2q-2.05 0-3.875.787q-1.825.788-3.187 2.151Q3.575 6.3 2.788 8.113Q2 9.925 2 12q0 1.825.6 3.463q.6 1.637 1.7 2.937Z">
                                </path>
                            </svg>
                            <h1 class="font-bold text-lg font-oswald">Mess</h1>
                        </div>

                        <div v-show="userClick"
                            class="fixed inset-0 bg-black bg-opacity-50 transition-opacity duration-300">
                            <div class="user-profile-drawer transform transition-transform duration-300">
                                <div class="bg-background">
                                    <img src="../assets/XXX.png" @click="toggleUserProfile"
                                        class="cancle-img pt-8 pl-4 w-12 h-16" />
                                    <div class="flex justify-center"> <img src="../assets/team/Hanan Pic 1.jpg"
                                            class="home-image" alt="hanan" />
                                    </div>
                                    <h1 class="text-center font-bold text-3xl pb-4 font-oswald text-secondary">Hanan
                                    </h1>
                                </div>
                                <div class="head-bio flex space-x-6 p-6">
                                    <h1 class="font-bold font-oswald text-lg">bio:</h1>
                                    <p class="text-justify font-robot text-md text-lg ">dventurous soul with a passion
                                        for
                                        exploring the
                                        unknown.
                                        Enthusiastic traveler, amateur photographer, and aspiring foodie.</p>
                                </div>
                                <div class="bg-primary text-white p-4">
                                    <div class="flex items-center font-robot space-x-10 pl-4">
                                        <h1 class="font-bold text-oswald text-lg">Name:</h1>
                                        <h1>ADDISALEM MEKURIA</h1>
                                    </div>
                                    <div class="flex items-center font-robot space-x-8 pl-4">
                                        <h1 class="font-bold text-oswald text-lg">Gender:</h1>
                                        <h1>M</h1>
                                    </div>
                                    <div class="flex items-center font-robot space-x-4 pl-4">
                                        <h1 class="font-bold text-oswald text-lg">Phone no:</h1>
                                        <h1>911913002</h1>
                                    </div>
                                </div>

                                <div class="flex justify-between p-6">
                                    <div class="flex justify-center" @click="Editdialogmethod">
                                        <div
                                            class="etcare-button xs:pt-1 xs:pb-1 xs:pl-5 xs:pr-5 md:pt-2 md:pb-2 md:pl-8 md:pr-8 edit-button flex items-center space-x-4">
                                            <svg xmlns="http://www.w3.org/2000/svg" width="1.4em" height="1.4em"
                                                viewBox="0 0 24 24">
                                                <path fill="currentColor"
                                                    d="M4 20v-2.8q0-.85.438-1.562T5.6 14.55q1.55-.775 3.15-1.162T12 13q.925 0 1.825.113t1.8.362l-1.675 1.7q-.5-.075-.975-.125T12 15q-1.4 0-2.775.338T6.5 16.35q-.225.125-.363.35T6 17.2v.8h6v2zm10 1v-3.075l5.525-5.5q.225-.225.5-.325t.55-.1q.3 0 .575.113t.5.337l.925.925q.2.225.313.5t.112.55t-.1.563t-.325.512l-5.5 5.5zm7.5-6.575l-.925-.925zm-6 5.075h.95l3.025-3.05l-.45-.475l-.475-.45l-3.05 3.025zm3.525-3.525l-.475-.45l.925.925zM12 12q-1.65 0-2.825-1.175T8 8t1.175-2.825T12 4t2.825 1.175T16 8t-1.175 2.825T12 12m0-2q.825 0 1.413-.587T14 8t-.587-1.412T12 6t-1.412.588T10 8t.588 1.413T12 10m0-2">
                                                </path>
                                            </svg>

                                            <h1>Edit</h1>
                                        </div>
                                    </div>
                                    <div class="flex justify-center">
                                        <div @click="logoutdialogmethod"
                                            class="etcare-button xs:pt-1 xs:pb-1 xs:pl-5 xs:pr-5 md:pt-2 md:pb-2 md:pl-8 md:pr-8 footer-button flex items-center space-x-4 edit-button">
                                            <svg xmlns="http://www.w3.org/2000/svg" width="1.4em" height="1.4em"
                                                viewBox="0 0 24 24">
                                                <path
                                                    d="M12 3c-4.963 0-9 4.037-9 9v.001l5-4v3h7v2H8v3l-5-4C3.001 16.964 7.037 21 12 21s9-4.037 9-9s-4.037-9-9-9z"
                                                    fill="currentColor"></path>
                                            </svg>
                                            <h1>Log Out</h1>
                                        </div>
                                    </div>

                                </div>

                            </div>

                            <div v-if="logoutdialog" class="dialog-overlay">
                                <div class="dialog">
                                    <h3>Confirm Logout</h3>
                                    <p>Are you sure you want to log out?</p>
                                    <div class="dialog-actions">
                                        <button @click="confirmLogout" class="text-secondary">Yes, Logout</button>
                                        <button @click="logoutdialogmethod">Cancel</button>
                                    </div>
                                </div>
                            </div>

                            <div v-if="profiledialog"
                                class="fixed inset-0 z-50 flex items-center justify-center bg-black bg-opacity-50">
                                <div class="text-primary bg-white rounded-lg shadow-md w-full max-w-md p-6">
                                    <h2 class="text-2xl font-bold font-oswald text-primary mb-4">Edit Profile</h2>
                                    <form @submit.prevent="updateProfile">
                                        <div class="mb-4">
                                            <label for="username"
                                                class="block text-sm font-medium text-gray-700">Username</label>
                                            <input v-model="form.username" type="text" id="username" required
                                                class="mt-1 block w-full p-2 border border-gray-300 rounded-md focus:ring-blue-500 focus:border-blue-500" />
                                        </div>
                                        <div class="mb-4">
                                            <label for="password"
                                                class="block text-sm font-medium text-gray-700">Password</label>
                                            <input v-model="form.password" type="password" id="password" required
                                                class="mt-1 block w-full p-2 border border-gray-300 rounded-md focus:ring-blue-500 focus:border-blue-500" />
                                        </div>
                                        <div class="mb-4">
                                            <label for="confirmPassword"
                                                class="block text-sm font-medium text-gray-700">Confirm
                                                Password</label>
                                            <input v-model="form.confirmPassword" type="password" id="confirmPassword"
                                                required
                                                class="mt-1 block w-full p-2 border border-gray-300 rounded-md focus:ring-blue-500 focus:border-blue-500" />
                                        </div>
                                        <button type="submit"
                                            class=" w-full bg-primary text-white py-2 rounded-md hover:bg-blue-600 transition duration-300">
                                            <div class="flex items-center space-x-6 justify-center font-bold">
                                                <svg xmlns="http://www.w3.org/2000/svg" width="1.25em" height="1.25em"
                                                    viewBox="0 0 24 24">
                                                    <path fill="currentColor"
                                                        d="M4 20v-2h2.75l-.4-.35q-1.225-1.225-1.787-2.662T4 12.05q0-2.775 1.663-4.937T10 4.25v2.1Q8.2 7 7.1 8.563T6 12.05q0 1.125.425 2.188T7.75 16.2l.25.25V14h2v6zm10-.25v-2.1q1.8-.65 2.9-2.212T18 11.95q0-1.125-.425-2.187T16.25 7.8L16 7.55V10h-2V4h6v2h-2.75l.4.35q1.225 1.225 1.788 2.663T20 11.95q0 2.775-1.662 4.938T14 19.75">
                                                    </path>
                                                </svg>
                                                <h1> Update Profile
                                                </h1>
                                            </div>
                                        </button>
                                        <button type="button" @click="Editdialogmethod"
                                            class="mt-4 w-full text-primary hover:text-secondary">
                                            Cancel
                                        </button>
                                    </form>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </header>

        <div class="bg-background text-white h-100">
            <slot />
        </div>

        <footer class="bg-primary font-roboto text-white ">
            <div class="body-padding_margin">
                <div class="container">
                    <div class="grid grid-cols-1 md:grid-cols-4 gap-4 pt-10 pb-10">

                        <div class="space-y-3 ">
                            <div class="items-center flex space-x-5">
                                <svg xmlns="http://www.w3.org/2000/svg" width="2em" height="2em" viewBox="0 0 24 24">
                                    <path fill="currentColor"
                                        d="M12 20.556q-.235 0-.47-.077t-.432-.25q-1.067-.981-2.164-2.185q-1.096-1.203-1.99-2.493t-1.468-2.633t-.572-2.622q0-3.173 2.066-5.234Q9.037 3 12 3t5.03 2.062q2.066 2.061 2.066 5.234q0 1.279-.572 2.613q-.572 1.333-1.458 2.632q-.885 1.3-1.981 2.494T12.92 20.21q-.191.173-.434.26q-.244.086-.487.086m.004-8.825q.667 0 1.14-.476q.472-.475.472-1.143t-.476-1.14t-1.143-.472t-1.14.476t-.472 1.143t.475 1.14t1.144.472">
                                    </path>
                                </svg>
                                <a href="https://maps.app.goo.gl/Bim8BvzZjeQAjKTU8" class="links" target="_blank">
                                    <h4>Addis Ababa, Ethiopia</h4>
                                </a>
                            </div>

                            <div class="items-center flex space-x-5">
                                <svg xmlns="http://www.w3.org/2000/svg" width="2em" height="2em" viewBox="0 0 24 24">
                                    <g fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round"
                                        stroke-width="2">
                                        <path stroke-dasharray="64" stroke-dashoffset="64"
                                            d="M4 5h16c0.55 0 1 0.45 1 1v12c0 0.55 -0.45 1 -1 1h-16c-0.55 0 -1 -0.45 -1 -1v-12c0 -0.55 0.45 -1 1 -1Z">
                                            <animate fill="freeze" attributeName="stroke-dashoffset" dur="0.6s"
                                                values="64;0"></animate>
                                        </path>
                                        <path stroke-dasharray="24" stroke-dashoffset="24" d="M3 6.5l9 5.5l9 -5.5">
                                            <animate fill="freeze" attributeName="stroke-dashoffset" begin="0.6s"
                                                dur="0.2s" values="24;0"></animate>
                                        </path>
                                    </g>
                                </svg>
                                <a href="mailto:Etcare@gmail.com" class="links">
                                    <h4>Etcare@gmail.com</h4>
                                </a>
                            </div>

                            <div class="items-center flex space-x-5">
                                <svg xmlns="http://www.w3.org/2000/svg" width="2em" height="2em" viewBox="0 0 24 24">
                                    <path fill="currentColor"
                                        d="M19.95 21q-3.125 0-6.175-1.362t-5.55-3.863t-3.862-5.55T3 4.05q0-.45.3-.75t.75-.3H8.1q.35 0 .625.238t.325.562l.65 3.5q.05.4-.025.675T9.4 8.45L6.975 10.9q.5.925 1.187 1.787t1.513 1.663q.775.775 1.625 1.438T13.1 17l2.35-2.35q.225-.225.588-.337t.712-.063l3.45.7q.35.1.575.363T21 15.9v4.05q0 .45-.3.75t-.75.3">
                                    </path>
                                </svg>

                                <a href="tel:+251917550560" class="links">
                                    <h4>+251-91-755-0560</h4>
                                </a>
                            </div>

                        </div>


                        <div>
                            <h4 class="mb-4 font-bold font-oswald">COMPANY</h4>
                            <ul class="space-y-2">
                                <li>
                                    <nuxt-link to="/about" class="links">About</nuxt-link>
                                </li>
                                <li>
                                    <nuxt-link to="/service" class="links">Service</nuxt-link>
                                </li>
                                <li>
                                    <nuxt-link to="/blog" class="links">Blog</nuxt-link>
                                </li>
                                <li>
                                    <nuxt-link to="/service/saving" class="links">Saving</nuxt-link>
                                </li>
                                <li>
                                    <nuxt-link to="/service/equb" class="links">Equb</nuxt-link>
                                </li>
                                <li>
                                    <nuxt-link to="/service/loan" class="links">Loan</nuxt-link>
                                </li>
                            </ul>
                        </div>


                        <div class="space-y-3">
                            <h4 class="mb-4 font-bold font-oswald">LATEST NEWS</h4>
                            <footerblogco imageSrc="../_nuxt/assets/dall1.png"
                                description="Empowering Members Through Financial Education" date="21th Joly 2017" />
                            <footerblogco imageSrc="../_nuxt/assets/dall2.png"
                                description="Empowering Members Through Financial Education" date="21th Joly 2017" />
                            <footerblogco imageSrc="../_nuxt/assets/dall3.png"
                                description="Empowering Members Through Financial Education" date="21th Joly 2017" />
                        </div>

                        <div>
                            <h5 class="text-justify mb-4 font-bold ">Contact your nearest Etcare SACCO branch to receive
                                your
                                account username and password.</h5>
                            <div class="flex justify-center pt-5">
                                <nuxt-link to="/contact"
                                    class="etcare-button xs:pt-1 xxxs:pb-1 xxxs:pl-5 xxxs:pr-5 md:pt-2 md:pb-2 md:pl-8 md:pr-8 footer-button flex items-center space-x-4">
                                    <svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em"
                                        viewBox="0 0 20 20">
                                        <path fill="currentColor"
                                            d="M17 11v3l-3-3H8a2 2 0 0 1-2-2V2c0-1.1.9-2 2-2h10a2 2 0 0 1 2 2v7a2 2 0 0 1-2 2zm-3 2v2a2 2 0 0 1-2 2H6l-3 3v-3H2a2 2 0 0 1-2-2V8c0-1.1.9-2 2-2h2v3a4 4 0 0 0 4 4z">
                                        </path>
                                    </svg>
                                    <h1> contact us</h1>
                                </nuxt-link>
                            </div>

                            <div class="flex justify-center">
                                <div class="flex space-x-3 pt-5">
                                    <nuxt-link to="https://web.facebook.com/etcaresacco" target="_blank"><svg
                                            class="socialM" xmlns="http://www.w3.org/2000/svg" width="2em" height="2em"
                                            viewBox="0 0 24 24">
                                            <path fill="currentColor"
                                                d="M22 12c0-5.52-4.48-10-10-10S2 6.48 2 12c0 4.84 3.44 8.87 8 9.8V15H8v-3h2V9.5C10 7.57 11.57 6 13.5 6H16v3h-2c-.55 0-1 .45-1 1v2h3v3h-3v6.95c5.05-.5 9-4.76 9-9.95">
                                            </path>
                                        </svg></nuxt-link>
                                    <nuxt-link to="https://www.youtube.com/@etcarebeautyandcosmeticssales"
                                        target="_blank">
                                        <svg class="socialM" xmlns="http://www.w3.org/2000/svg" width="2em" height="2em"
                                            viewBox="0 0 24 24">
                                            <path fill="currentColor"
                                                d="M12.244 4c.534.003 1.87.016 3.29.073l.504.022c1.429.067 2.857.183 3.566.38c.945.266 1.687 1.04 1.938 2.022c.4 1.56.45 4.602.456 5.339l.001.152v.174c-.007.737-.057 3.78-.457 5.339c-.254.985-.997 1.76-1.938 2.022c-.709.197-2.137.313-3.566.38l-.504.023c-1.42.056-2.756.07-3.29.072l-.235.001h-.255c-1.13-.007-5.856-.058-7.36-.476c-.944-.266-1.687-1.04-1.938-2.022c-.4-1.56-.45-4.602-.456-5.339v-.326c.006-.737.056-3.78.456-5.339c.254-.985.997-1.76 1.939-2.021c1.503-.419 6.23-.47 7.36-.476zM9.999 8.5v7l6-3.5z">
                                            </path>
                                        </svg></nuxt-link>
                                    <nuxt-link to="https://vm.tiktok.com/ZMhQxWYC7/" target="_blank"> <svg
                                            class="socialM" xmlns="http://www.w3.org/2000/svg" width="2em" height="2em"
                                            viewBox="0 0 24 24">
                                            <path
                                                d="M19.59 6.69a4.83 4.83 0 0 1-3.77-4.25V2h-3.45v13.67a2.89 2.89 0 0 1-5.2 1.74a2.89 2.89 0 0 1 2.31-4.64a2.93 2.93 0 0 1 .88.13V9.4a6.84 6.84 0 0 0-1-.05A6.33 6.33 0 0 0 5 20.1a6.34 6.34 0 0 0 10.86-4.43v-7a8.16 8.16 0 0 0 4.77 1.52v-3.4a4.85 4.85 0 0 1-1-.1z"
                                                fill="currentColor"></path>
                                        </svg></nuxt-link>

                                    <nuxt-link to="https://t.me/etcaresacco" target="_blank"><svg class="socialM"
                                            xmlns="http://www.w3.org/2000/svg" width="2em" height="2em"
                                            viewBox="0 0 24 24">
                                            <path
                                                d="M9.78 18.65l.28-4.23l7.68-6.92c.34-.31-.07-.46-.52-.19L7.74 13.3L3.64 12c-.88-.25-.89-.86.2-1.3l15.97-6.16c.73-.33 1.43.18 1.15 1.3l-2.72 12.81c-.19.91-.74 1.13-1.5.71L12.6 16.3l-1.99 1.93c-.23.23-.42.42-.83.42z"
                                                fill="currentColor"></path>
                                        </svg></nuxt-link>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <div class="textcopy">
                <div class="body-padding_margin">
                    <div class="container">
                        <div
                            class="grid grid-cols-1 md:grid-cols-2 gap-4 xxxs:py-4 justify-around w-full items-center text-primary md:py-6 xxl:py-8">
                            <div>
                                <nuxt-link to="/"> <img src="../assets/Etcare_logo1-removebg.png" alt="etcare logo" />
                                </nuxt-link>
                            </div>
                            <div>
                                <h4 class="font-bold md:text-end">© 2024 by EtCare Sacco. All Rights Reserved.</h4>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </footer>
    </div>
</template>

<script setup>
import { ref, reactive, onMounted, onBeforeUnmount } from 'vue';
import { useAuthStore } from '../stores/auth';
import { useRouter } from 'vue-router';

const headerBackgroundColor = ref('rgba(255, 255, 255, 0.55)');
const login = ref(true);
const userClick = ref(false);
const logoutdialog = ref(false);
const profiledialog = ref(false);
const isMenuOpen = ref(false);
const openMenuService = ref(false);
const form = reactive({
    username: '',
    password: '',
    confirmPassword: '',
});
const authStore = useAuthStore();
const router = useRouter();

const handleScroll = () => {
    if (window.scrollY > 100) {
        headerBackgroundColor.value = '#fff';
    } else {
        headerBackgroundColor.value = 'rgba(255, 255, 255, 0.55)';
    }
};

const toggleMenu = () => {
    isMenuOpen.value = !isMenuOpen.value;
}

const closeMenu = () => {
    isMenuOpen.value = !isMenuOpen.value;
    openMenuService.value = false;
}
const toggleMenuservice = () => {
    openMenuService.value = !openMenuService.value;
}

const closeMenuservice = () => {
    openMenuService.value = !openMenuService.value;
    isMenuOpen.value = false;
}

// User actions
const toggleUserProfile = () => {
    userClick.value = !userClick.value;
};

const confirmLogout = () => {
    router.push('/login');
};

const logoutdialogmethod = () => {
    logoutdialog.value = !logoutdialog.value;
};

const Editdialogmethod = () => {
    profiledialog.value = !profiledialog.value;
};

const closeModal = () => {
    // Emit a custom event if necessary
    // Use `emit` function for emits in <script setup> if needed
};

const updateProfile = () => {
    if (form.password !== form.confirmPassword) {
        alert("Passwords do not match!");
        return;
    }
    form.username = '';
    form.password = '';
    form.confirmPassword = '';
    closeModal();
};

const user = ref({});
const loading = ref(true);
const { $axios } = useNuxtApp();
const error = ref(null);
// Lifecycle hooks
onMounted(async () => {
    // try {
    //     const response = await $axios.get('/userlogin/');

    //     user.value = response.data; // Set user data
    //     console.log(user);
    // } catch (err) {
    //     error.value = err.response?.data?.detail || err.message; // Handle errors
    // } finally {
    //     loading.value = false; // End loading state
    // }
    window.addEventListener('scroll', handleScroll);
    const token = authStore.accessToken;
    login.value = !token;
});

onBeforeUnmount(() => {
    window.removeEventListener('scroll', handleScroll);
});
</script>

<style>
@media (min-width: 200px) {
    .body-padding_margin {
        padding: 0 1rem;
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
}

@media (min-width: 1200px) {
    .body-padding_margin {
        padding: 0 5rem;
    }
}

/* global.css */
.container {
    max-width: 1240px;
    /* Adjust this value as per your design */
    margin: 0 auto;
    /* Center the container */
    padding: 0 1rem;
    /* Add some padding for smaller screens */
}


.user-profile-drawer {
    position: absolute;
    top: 0;
    right: 0;
    width: 30%;
    min-height: 100vh;
    background: theme('colors.primary');
}

.head-bio {
    background: #FFDFDF;
}

.home-image {
    border-radius: 50%;
    width: 170px;
    height: 170px;
    border: 4px solid theme('colors.secondary');
}

.cancle-img {
    cursor: pointer;
}

.web-body {
    padding: 0;
    margin: 0;
    background-color: theme('colors.background');
}

.links:hover {
    color: theme('colors.secondary');
}

.etcare-button {
    background-color: theme('colors.primary');
    color: theme('colors.white');
    border-radius: 10px 10px 10px 0;
    border: none;
    cursor: pointer;
}

.edit-button {
    background-color: theme('colors.background');
    color: theme('colors.primary');
    border-radius: 1px;
}

.etcare-button:hover {
    background-color: theme('colors.background');
    color: theme('colors.secondary');
}

.footer-button {
    font-size: 0.8rem;
    border-radius: 1px;
    background-color: theme('colors.secondary');
    color: theme('colors.background');

}

.textcopy {
    background-color: theme('colors.background');
}

.footerpadding {
    padding: 0 4rem;
    height: 440px;
}

.socialM {
    transition: transform .3s ease-in-out;
}

.socialM:hover {
    transform: translateY(-15%);
    color: theme('colors.secondary');
}

.dropdown {
    position: absolute;
    background-color: white;
    /* Replace with theme('colors.white') */
    width: 25%;
    border-top: solid 1px #ccc;
    /* Replace with theme('colors.secondary') */
    top: 60%;
    visibility: hidden;
    opacity: 0;
    transition: opacity 1s, visibility 1s;
}

.dropdown-link:hover .dropdown {
    visibility: visible;
    opacity: 1;
}

.dropdown li:hover {
    color: theme('colors.secondary');
}

.dropdown li {
    padding: 0.5rem 1rem;
    position: relative;
    border-bottom: solid 1px theme('colors.secondary');
    overflow: hidden;
}

.dropdown li::before {
    content: '';
    background-image: linear-gradient(to right, transparent, theme('colors.primary'));
    width: 0;
    position: absolute;
    bottom: 0;
    height: 100%;
    left: 0;
    transition: width 0.65s ease;
}

.dropdown li:hover::before {
    width: 100%;
}

.user-profile {
    cursor: pointer;
}

.dialog-overlay {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: rgba(0, 0, 0, 0.5);
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 1000;
}

.dialog {
    background: white;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
    text-align: center;
}

.dialog-actions {
    margin-top: 20px;
}

.dialog-actions button {
    margin: 0 10px;
}
</style>