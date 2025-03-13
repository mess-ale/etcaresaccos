<template>
    <div class="body-padding_margin">
        <div class="container">
            <div class="py-8">
                <div class="grid grid-cols-1 md:grid-cols-5 gap-8 items-center justify-center">
                    <img v-for="(photo, index) in photos" :key="index" :src="photo.url" alt="Photo" class="hover-photo"
                        @click="showPhoto(index)">
                </div>
                
                <div v-if="selectedPhoto !== null" class="modal" @click="closeModal">
                    <img :src="photos[selectedPhoto].url" alt="Selected Photo" class="modal-img">
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            photos: [
                { url: '/photo/gallary-1.jpg' },
                { url: '/photo/gallary-2.jpg' },
                { url: '/photo/gallary-3.jpg' },
                { url: '/photo/gallary-4.jpg' },
                { url: '/photo/gallary-5.jpg' },
            ],
            selectedPhoto: null
        };
    },
    methods: {
        showPhoto(index) {
            this.selectedPhoto = index;
        },
        closeModal() {
            this.selectedPhoto = null;
        }
    }
};
</script>

<style>
.hover-photo {
    cursor: pointer;
    width: 100%;
    height: 15rem;
    background-size: cover;
    background-position: center;
    transition: transform 0.3s ease-in-out;
}

.hover-photo:hover {
    transform: scale(1.05);
}

.modal {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.7);
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 11;
}


@media (min-width: 0) {
    .modal-img {
        width: 90%;
        height: 60%;
    }
}

@media (min-width: 1024px) {
    .modal-img {
        width: 60%;
        height: 80%;
    }
}
</style>