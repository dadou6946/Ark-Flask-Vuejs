<template>
    <div class="container">

        <h1 class="center-align">{{ pageTitle3 }}</h1>
        <br><div class="divider"></div><br>

        <div class="row">
            <div class="col m7 center-align">

                <div>
                  <p>{{ instruction }}</p>
                </div>

                <div>
                    <button v-for="ancien in anciens"
                        v-bind:class="{ 'teal': !ancien.selected, 'red': ancien.selected }"
                        class="waves-effect waves-light btn"
                        @click="chooseAcien(ancien)"
                        @mouseover="mouseOver(ancien.name)"
                        @mouseleave="hovered=''">
                    {{ ancien.name }}
                    </button>
                </div>

                <br><div class="divider"></div><br>

                <div>
                  <input type="submit" class="btn" :disabled="!preventConfirm" @click="continueAction" value="Confirmer">
                </div>

                <br><div class="divider"></div><br>
            </div>

            <div class="col m5 center-align">
                <transition name="fade">
                    <div v-if="hovered !=''"
                        id="image_content"
                        class="center-align z-depth-3">
                        <img id="image-preview" :src="imagePath">
                    </div>
                </transition>
            </div>

        </div>
        <div class="row">

            <div class="col m4 center-align">
            </div>
        </div>

    </div>
</template>

<script>
export default {
  data() {
    return {

      pageTitle3: 'Choix du Grand Ancien',
      instruction: 'Veuillez choisir le Grand Ancien pour cette partie',
      anciens: [
        { name: 'Yig', difficulty: 'easy', selected: false },
        { name: 'Cthulhu', difficulty: 'hard', selected: false },
        { name: 'Daoloth', difficulty: 'medium', selected: false },
        { name: 'Hastur', difficulty: 'easy', selected: false },
      ],
      ancienChoice: '',
      preventConfirm: false,
      imagePath: '',
      hovered: '',
    };
  },
  methods: {

    submit() {
      // Envoi des données au server
      // Diriger vers le nouveau composant
    },


    chooseAcien(ancien) {
      if (ancien.selected == true) {
        ancien.selected = false;
        this.ancienChoice = '';
        this.preventConfirm = false;
      } else {
        this.anciens.forEach((anc) => {
          anc.selected = false;
        });
        this.ancienChoice = ancien.name;
        ancien.selected = true;
        this.preventConfirm = true;
      }
    },
    continueAction() {
      // console.log('ici')
      this.$router.push('set-clues');
    },
    mouseOver(name) {
      this.hovered = true;
      this.imagePath = `/image/sheet/ancient/${name.replace(' ', '')}.jpg`;
    },
  },
};
</script>

<style>
    #image_content {
        height: 680px;
        width: 100%;
        padding: 25px;
    }

    #image-preview {
        height: 100%;
        width: auto;
        margin: auto;
    }
    /*TRANSITIONS*/
    .fade-enter-active, .fade-leave-active {
        transition: opacity .75s;
    }
    .fade-enter, .fade-leave-to
    {
        opacity: 0;
    }
</style>
