<template>

</template>

<script>
export default {
  data() {
    return {

    };
  },
  methods: {

    log(message) {
      console.log(message);
    },

    continueAction() {
      // console.log('ici')
      this.$router.push('choose-ancient');
    },
  },
};

</script>

<style>

</style>
