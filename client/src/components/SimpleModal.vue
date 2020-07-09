<template>
    <div id="modal1" class="modal open" tabindex="0">
        <div class="modal-content">
            <h4>{{ title }}</h4>
            <p class="center-align">{{ content }}</p>
            <slot></slot>
            <div class="right-align">
                <button class="waves-effect waves-light btn teal" @click="continueAction">{{ buttonText }}</button>
            </div>
        </div>
    </div>
</template>

<script>
export default {
  props: [
    'title',
    'content',
    'buttonText',
    'route',
  ],
  data() {
    return {

    };
  },
  methods: {
    continueAction() {
      // console.log('ici')
      this.$router.push(this.route);
    },
  },
};

</script>

<style>
    /*Modale*/
    #modal1
    {
        z-index: 999;
        display: block;
        opacity: 1;
        top: 25%;
        transform: scaleX(1) scaleY(1);
        height:168px;
        border-radius: 15px;
    }
</style>
