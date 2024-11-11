<template>
    <div>
        <h1>Counter: {{ count }}</h1>
        <button @click="increment">Increment</button>
        <button @click="decrement">Decrement</button>
        <button @click="reset">Reset</button>
    </div>
</template>

<!-- Uncomment to use JavaScript instead of TypeScript. -->
<!-- <script> -->
<!-- If you'd like to use the options API, remove the 'setup' keyword. -->
<script setup>
import { ref } from 'vue';
const count = ref(0);

const increment = () => {
    count.value++;
};

const decrement = () => {
    count.value--;
};

const reset = () => {
    count.value = 0;
};
</script>