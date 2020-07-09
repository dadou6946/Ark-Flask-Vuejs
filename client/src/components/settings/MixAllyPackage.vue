<template>
    <div class="container">

        <h1 class="center-align">{{ pageTitle }}</h1>
        <div class="divider"></div><br>

        <div class="row center-align">
            <div class="col m12">

                <div class="row">
                    <div class="col m12">
                        On crée la pile des alliés (11 pris au hasard).
                    </div>
                </div>

                <div class="row">
                    <div class="col m12">
                        <img id="ally-img" src="/image/card/type/ally.jpg" alt="Alliés" class="z-depth-2">
                    </div>
                </div>

                <div class="divider"></div><br>

                <div>
                  <div class="waves-effect waves-light btn" @click="continueAction">Etape suivante</div>
                </div>

            </div>

        </div>


    </div>
</template>

<script>
export default {
  data() {
    return {
      pageTitle: 'Récupération des alliés',
    };
  },
  methods: {
    continueAction() {
      // console.log('ici')
      this.$router.push('choose-ancient');
    },
  },
};
</script>

<style>
    img#ally-img
    {
        height: 150px;
        width: auto;
    }
</style>
