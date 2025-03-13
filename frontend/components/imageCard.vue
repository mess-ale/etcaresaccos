<template>
    <div class="cover cover-service-img">
        <div class="text">
            <h1 class="text-secondary font-oswald font-bold text-5xl">{{ text }}</h1>
        </div>
    </div>
    <img src="/Group 40.png" class="pt-4 pb-12 image-class" alt="line header" />
</template>

<script>
export default {
    props: {
        text: {
            type: String,
            required: true
        }
    }
};
</script>

<style scoped>
.cover {
    background-image: url('/assets/2.jpg');
    height: 23rem;
    display: flex;
    align-items: center;
    background-size: cover;
    background-position: center;
}

.text {
    width: 100%;
    display: flex;
    text-align: center;
    justify-content: center;
}

.image-class {
    width: 100%;
}
</style>