<template>
    <div class="container">

        <h1 class="center-align">{{ pageTitle }}</h1>
        <div class="divider"></div>

        <div class="row"><br>

            <div class="col m12 center-align">

                <div v-for="(investigator,index) of investigators">
                    <span v-html="investigator.name"></span>
                    (joueur <span v-html="index + 1"></span>)
                    commence la partie avec :
                    <span v-html="investigator.resistance"></span> <img class="heart_icon" src="image/icon/red_heart_icon.png" alt="health">
                     et
                     <span v-html="investigator.sanity"></span> <img class="heart_icon" src="image/icon/blue_heart_icon.png" alt="sanity">.
                    <br><br>
                </div>

                <br>

                <button class="waves-effect waves-light btn teal"
                    @click="continueAction">Etape suivante</button>
            </div>
        </div>

    </div>
</template>

<script>
export default {
  data() {
    return {
      pageTitle: 'Attribution des résistances et de la santé mentale',
      playerNumber: 4,
      investigators: [
        { name: 'Joe Diamond', resistance: 6, sanity: 4 },
        { name: 'Peggy Green', resistance: 4, sanity: 6 },
        { name: 'Jenny Barnes', resistance: 4, sanity: 6 },
        { name: 'Francis Sailor', resistance: 4, sanity: 6 },
      ],
    };
  },
  methods: {

    log(message) {
      console.log(message);
    },

    continueAction() {
      // console.log('ici')
      this.$router.push('set-properties');
    },
  },
};

</script>

<style>
  img.heart_icon
  {
    height: 20px;
    margin-left: 5px;
  }
</style>
