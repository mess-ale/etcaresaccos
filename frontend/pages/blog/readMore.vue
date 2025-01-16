<template>
    <div class="body-padding_margin blog-image">
        <div class="xxxs:space-y-2 md:space-y-4 xxxs:pt-24 md:pt-32 xxxs:pb-12 md:pb-20 text-primary md:w-2/4 text-justify">
            <img class="blog-image-card" src="../../assets/event.PNG" />
            <div class="flex justify-between blog-title gap-8">
                <h1 class="text-secondary font-bold xxxs:text-xs md:text-2xl font-oswald">Grand Appreciation and Recognition Program
                </h1>
                <h1 class="text-secondary font-bold xxxs:text-xs md:text-2xl font-oswald">Saturday, November 23</h1>
            </div>
            <p class=" xxxs:text-xs md:text-xl">Join us for a day of appreciation and recognition as we celebrate outstanding achievements and honor
                remarkable individuals at the "Grand Appreciation and Recognition Program."</p>
            <ul class=" xxxs:text-xs md:text-xl">
                <h1>Event Details:</h1>
                <li><strong>Date:</strong> Saturday, November 3</li>
                <li><strong>Time:</strong> Starting from 9:00 AM</li>
                <li><strong>Venue:</strong> Millennium Hall</li>
            </ul>

            <p class=" xxxs:text-xs md:text-xl">This special program will include inspiring speeches, award presentations, and an opportunity to connect
                with like-minded individuals committed to excellence. The event is open to all who wish to be part of a
                day dedicated to celebrating hard work, success, and the spirit of achievement.
            </p>
            <p class=" xxxs:text-xs md:text-xl">Don’t miss this memorable occasion! Tickets are available for entry. Secure your spot and be a part of
                this remarkable gathering.</p>
        </div>
    </div>
</template>

<style>
.blog-image-card {
  width: 100%;
  height: auto;
  background-size: cover;
  background-position: center;
}

.blog-image {
    justify-content: center;
    display: flex;
}

.blog-title {
    border-bottom: solid 1px theme('colors.primary');
    padding: 0.5rem 0;
}

.blog-image img {
    border-radius: 0.75rem;
}

ul li {
    padding-left: 20px;
}
</style>