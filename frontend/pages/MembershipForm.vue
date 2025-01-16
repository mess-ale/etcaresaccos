<template>
    <div>
        <ServiceCard text="Membership Form" imgservice="../_nuxt/assets/form.jpg" />

        <div class="body-padding_margin">
            <div
                class="my-div max-w-4xl pb-4 mb-12 mx-auto p-6 bg-white text-primary shadow-md bb-primary rounded-md justify-between flex font-robot gap-2">
                <nuxt-link class="links xxxs:text-sm md:text-lg" to="#bank">Bank Accounts</nuxt-link>
                <nuxt-link class="links xxxs:text-sm md:text-lg" to="#eligibility">Eligibility Criteria</nuxt-link>
                <nuxt-link class="links xxxs:text-sm md:text-lg" to="#benefits">Benefits of Membership</nuxt-link>
                <nuxt-link class="links xxxs:text-sm md:text-lg" to="#becoming">Becoming a Member</nuxt-link>
            </div>

            <div class="my-div max-w-4xl pb-8 mb-12 mx-auto p-6 bg-white text-primary shadow-md rounded-md font-robot">

                <h2 class="xxxs:text-2xl md:text-3xl font-bold text-center text-secondary mb-12 font-oswald">EtCare
                    Membership Form</h2>
                <form @submit.prevent="handleSubmit">
                    <!-- Personal Details -->
                    <div class="grid grid-cols-1 sm:grid-cols-3 gap-4 mb-6">
                        <div>
                            <label for="firstName" class="block text-sm font-medium text-primary font-bold">First
                                Name</label>
                            <input v-model="form.firstName" id="firstName" type="text"
                                class="mt-1 p-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-green-500 focus:border-green-500 sm:text-sm"
                                placeholder="First Name" required />
                        </div>
                        <div>
                            <label for="fatherName" class="block text-sm font-medium text-primary font-bold">Father
                                Name</label>
                            <input v-model="form.fatherName" id="fatherName" type="text"
                                class="mt-1 p-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-green-500 focus:border-green-500 sm:text-sm"
                                placeholder="Father Name" required />
                        </div>
                        <div>
                            <label for="grandfatherName"
                                class="block text-sm font-medium text-primary font-bold">Grandfather
                                Name</label>
                            <input v-model="form.grandfatherName" id="grandfatherName" type="text"
                                class="mt-1 p-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-green-500 focus:border-green-500 sm:text-sm"
                                placeholder="Grandfather Name" required />
                        </div>
                    </div>

                    <!-- Email -->
                    <div class="mb-6">
                        <label for="email" class="block text-sm font-medium text-primary">Email Address</label>
                        <input v-model="form.email" id="email" type="email"
                            class="p-1 mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-green-500 focus:border-green-500 sm:text-sm"
                            placeholder="Email Address" required />
                    </div>

                    <!-- Email -->
                    <div class="mb-6">
                        <label for="phone" class="block text-sm font-medium text-primary">Phone Number</label>
                        <input v-model="form.phone" id="phone" type="tel"
                            class="p-1 mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-green-500 focus:border-green-500 sm:text-sm"
                            placeholder="Phone Number" required />
                    </div>

                    <!-- Saving Accounts -->
                    <fieldset class="mb-6">
                        <legend class="text-sm font-medium text-primary mb-2">Saving Accounts</legend>
                        <div class="flex space-x-4">
                            <label class="flex items-center">
                                <input type="radio" value="Time deposit" v-model="form.savingAccount"
                                    class="focus:ring-green-500 h-4 w-4 text-green-600 border-gray-300" />
                                <span class="ml-2 text-sm">Time deposit</span>
                            </label>
                            <label class="flex items-center">
                                <input type="radio" value="Children Saving" v-model="form.savingAccount"
                                    class="focus:ring-green-500 h-4 w-4 text-green-600 border-gray-300" />
                                <span class="ml-2 text-sm">Children Saving</span>
                            </label>
                            <label class="flex items-center">
                                <input type="radio" value="Business Saving" v-model="form.savingAccount"
                                    class="focus:ring-green-500 h-4 w-4 text-green-600 border-gray-300" />
                                <span class="ml-2 text-sm">Business Saving</span>
                            </label>
                        </div>
                    </fieldset>

                    <fieldset class="mb-6">
                        <legend class="text-sm font-medium text-primary mb-2">Loan Products</legend>
                        <div class="flex space-x-4">
                            <label class="flex items-center">
                                <input type="radio" value="Business Loan" v-model="form.loanProduct"
                                    class="focus:ring-green-500 h-4 w-4 text-green-600 border-gray-300" />
                                <span class="ml-2 text-sm">Business Loan</span>
                            </label>
                            <label class="flex items-center">
                                <input type="radio" value="Vehicle Loan" v-model="form.loanProduct"
                                    class="focus:ring-green-500 h-4 w-4 text-green-600 border-gray-300" />
                                <span class="ml-2 text-sm">Vehicle Loan</span>
                            </label>
                            <label class="flex items-center">
                                <input type="radio" value="Home Loan" v-model="form.loanProduct"
                                    class="focus:ring-green-500 h-4 w-4 text-green-600 border-gray-300" />
                                <span class="ml-2 text-sm">Home Loan</span>
                            </label>
                        </div>
                    </fieldset>

                    <div class="mb-6">
                        <label for="receipt" class="block text-sm font-medium text-primary">Attach Receipt of Bank
                            Deposit:</label>
                        <input id="receipt" type="file"
                            class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-green-500 focus:border-green-500 sm:text-sm"
                            @change="handleFileUpload" />
                    </div>

                    <div>
                        <button type="submit"
                            class="w-full bg-primary text-white py-2 px-4 rounded-md hover:bg-secondary focus:outline-none focus:ring-2 focus:ring-green-500 focus:ring-offset-2">
                            Submit
                        </button>
                    </div>
                </form>
            </div>

            <div id="bank" class="my-div max-w-4xl pb-8 mb-12 mx-auto p-6 bg-white text-primary shadow-md rounded-md">
                <h1 class="font-bold font-oswald text-secondary text-xl">Bank Accounts</h1>
                <ul class="bg-white shadow-md rounded-lg md:w-3/4 max-w-lg">
                    <li class="border-b border-gray-200 p-4">
                        <span class="font-medium text-gray-700">Commercial Bank Of Ethiopia</span>
                        <span class="block font-semibold">1000524668347</span>
                    </li>
                    <li class="border-b border-gray-200 p-4">
                        <span class="font-medium text-gray-700">Commercial Bank Of Ethiopia (Mudarebah Savings)</span>
                        <span class="block font-semibold">10005439084</span>
                    </li>
                    <li class="p-4">
                        <span class="font-medium text-gray-700">Dashen Bank (Savings Account)</span>
                        <span class="block font-semibold">5264357499011</span>
                    </li>
                </ul>
            </div>

            <div id="eligibility"
                class="my-div max-w-4xl pb-8 mb-12 mx-auto p-6 bg-white text-primary shadow-md rounded-md">
                <h1 class="mb-4 font-bold font-oswald text-secondary text-xl">Eligibility Criteria</h1>
                <ul class="list-decimal pl-6 space-y-3">
                    <li>
                        <p>Must be 18 years of age or older.</p>
                    </li>
                    <li>
                        <p>Willing to accept the society's bylaws, internal regulations, and guidelines.</p>
                    </li>
                    <li>
                        <p>Capable of paying the following:</p>
                        <ul class="list-disc pl-6 mt-2">
                            <li>Registration fee: <span class="font-semibold">1,500 ETB</span></li>
                            <li>Minimum initial savings: <span class="font-semibold">2,000 ETB</span></li>
                            <li>Monthly savings contribution: <span class="font-semibold">750 ETB</span></li>
                        </ul>
                    </li>
                    <li>
                        <p>Able to provide identification documents such as a national ID, driver's license, or
                            passport.
                        </p>
                    </li>
                </ul>
            </div>

            <div id="becoming"
                class="my-div max-w-4xl pb-8 mb-12 mx-auto p-6 bg-white text-primary shadow-md rounded-md">
                <h1 class="mb-4 font-bold font-oswald text-secondary text-xl">Becoming a Member</h1>
                <ul class="list-decimal pl-6 space-y-3">
                    <li>
                        <p>Complete the membership application online or visit our office to collect a membership
                            booklet.
                        </p>
                    </li>
                    <li>
                        <p>Submit any required additional information.
                        </p>
                    </li>
                    <li>
                        <p>Your application will be evaluated by our expert membership committee.
                        </p>

                    </li>
                    <li>
                        <p>Upon approval, you will officially join EtCare SACCO, receive a membership certificate, and
                            enjoy
                            full access to all our services, products, and benefits.</p>
                    </li>
                </ul>
            </div>

            <div id="benefits"
                class="my-div max-w-4xl pb-8 mb-12 mx-auto p-6 bg-white text-primary shadow-md rounded-md">
                <h1 class="mb-4 font-bold font-oswald text-secondary text-xl">Benefits of Membership</h1>
                <ul class="list-decimal pl-6 space-y-3">
                    <li>
                        <p>Comprehensive Financial Services: Gain access to diverse financial products, such as savings
                            accounts, loans, and insurance.</p>
                    </li>
                    <li>
                        <p>Profit-Sharing Opportunities: Participate in profit-sharing and earn dividends based on
                            Amigos
                            SACCO’s financial regulations.
                        </p>
                    </li>
                    <li>
                        <p>Competitive Interest Rates: Enjoy favorable interest rates on both savings and loans.

                        </p>

                    </li>
                    <li>
                        <p>Flexible Repayment Options: We understand that everyone’s financial needs are unique, so we
                            offer
                            flexible repayment schedules tailored to your situation.</p>
                    </li>
                    <li>
                        <p>Dedicated Support: Receive guidance and assistance from our friendly and professional staff.

                        </p>
                    </li>
                </ul>
            </div>
        </div>

    </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';

// Define reactive form data as a single object
const form = ref({
    firstName: '',
    fatherName: '',
    grandfatherName: '',
    email: '',
    phone: '',
    savingAccount: '',
    loanProduct: '',
    receipt: null,
});

// Nuxt composables
const { $axios } = useNuxtApp();
const router = useRouter();

// Handle file upload
const handleFileUpload = (event) => {
    const file = event.target.files[0];
    if (file) {
        form.value.receipt = file;
    }
};

// Handle form submission
const handleSubmit = async () => {
    const formData = new FormData();
    formData.append('first_name', form.value.firstName);
    formData.append('father_name', form.value.fatherName);
    formData.append('grandfather_name', form.value.grandfatherName);
    formData.append('email', form.value.email);
    formData.append('phone', form.value.phone);
    formData.append('saving_account', form.value.savingAccount);
    formData.append('loan_product', form.value.loanProduct);
    if (form.value.receipt) {
        formData.append('receipt', form.value.receipt);
    }

    try {
        const response = await $axios.post('/form-submissions/', formData, {
            headers: {
                'Content-Type': 'multipart/form-data',
            },
        });
        router.push('/success'); // Redirect on success
    } catch (error) {
    }
};
</script>

<style>
body {
    background-color: #f9fafb;
    font-family: Arial, sans-serif;
}

.my-div {
    border-bottom: 4px solid theme('colors.primary');
}
</style>