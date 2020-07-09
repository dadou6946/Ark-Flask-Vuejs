<template>

    <div class="container">

        <h1 class="center-align">{{ pageTitle }}</h1>

        <div class="divider"></div><br>

        <div class="row center-align">
            <div class="col-md-12">

                <div class="row">
                    <div class="col-md-12">
                        La tasse des monstres est créée.
                    </div>
                </div>

                <div class="row">
                    <div class="col-md-12">
                        <img class="z-depth-3" src="/image/monster/migo.jpg" alt="Migo">
                        <img class="z-depth-3" src="/image/monster/chthonien.jpg" alt="Chthonien">
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
      pageTitle: 'Création de la tasse des monstres',
    };
  },
  methods: {

    log(message) {
      console.log(message);
    },

    continueAction() {
      // console.log('ici')
      this.$router.push('mix-ancient-package');
    },
  },
};

</script>

<style>
        .btn {
            border-radius: 5px;
            margin: 2px;
            /*color: white;
            background-color: teal;*/
        }
        .selected {
            border: 3px solid lightgreen;
            -webkit-box-shadow: -3px -2px 5px 0px lightgreen;
            -moz-box-shadow: -3px -2px 5px 0px lightgreen;
            box-shadow: -3px -2px 5px 0px lightgreen;
        }
</style>
