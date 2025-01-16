<template>
  <div class="spin-wheel-container">
    <div class="wheel" :class="{ spinning: isSpinning }" @animationend="stopSpin">
      <div
        v-for="(item, index) in segments"
        :key="index"
        class="segment"
        :style="getSegmentStyle(index)"
      >
        <span>{{ item }}</span>
      </div>
    </div>
    <button @click="spinWheel">Spin</button>
  </div>
</template>

<script setup>
import { ref } from "vue";

const segments = ["Prize 1", "Prize 2", "Prize 3", "Prize 4", "Prize 5", "Prize 3", "Prize 4", "Prize 5", "Prize 3", "Prize 4", "Prize 5"];
const isSpinning = ref(false);

const spinWheel = () => {
  if (isSpinning.value) return;
  isSpinning.value = true;
};

const stopSpin = () => {
  isSpinning.value = false;
  alert("Spin Complete!");
};

const getSegmentStyle = (index) => {
  const rotation = (360 / segments.length) * index;
  return {
    transform: `rotate(${rotation}deg)`,
  };
};
</script>

<style scoped>
.spin-wheel-container {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.wheel {
  width: 300px;
  height: 300px;
  border-radius: 50%;
  border: 4px solid #000;
  position: relative;
  overflow: hidden;
  transform-origin: center;
}

.wheel.spinning {
  animation: spin 4s ease-out;
}

@keyframes spin {
  0% {
    transform: rotate(0);
  }
  100% {
    transform: rotate(1440deg); /* Adjust for spins */
  }
}

.segment {
  position: absolute;
  width: 50%;
  height: 50%;
  top: 0;
  left: 50%;
  transform-origin: 0 100%;
  background: #ffcccb;
  border: 1px solid #000;
}
</style>
