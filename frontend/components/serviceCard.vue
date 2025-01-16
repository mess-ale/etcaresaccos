<template>
    <div class="cover" :style="{ backgroundImage: `url(${imgservice})` }">
        <div class="text">
            <h1 class="text-secondary font-oswald font-bold xxxs:text-3xl md:text-4xl">{{ text }}</h1>
        </div>
    </div>
    <img src="../assets/Group 40.png" class="pt-4 pb-12 image-class" alt="line header" />
</template>

<script>
export default {
    props: {
        text: {
            type: String,
            required: true
        },
        imgservice: {
            type: String,
            required: true,
        }
    }
};
</script>

<style scoped>
@media (min-width: 0) {
    .cover {
        height: 45vh;
    }
}
@media (min-width: 740px) {
    .cover {
        height: 58vh;
    }
}
@media (min-width: 1024px) {
    .cover {
        height: 70vh;
    }
}

.cover {
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