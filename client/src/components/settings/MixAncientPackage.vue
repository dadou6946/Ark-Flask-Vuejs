<template>

    <div class="container">

        <h1 class="center-align">{{ pageTitle }}</h1>

        <div class="divider"></div><br>

        <div class="row center-align">
            <div class="col m12">

                <div class="row">
                    <div class="col m12">
                        Les paquets de l'ancien sont mélangés.
                    </div>
                </div>

                <div class="row">
                    <div class="col m12 center-align">
                        <img class="responsive-img card-image" style="width: 100px;border-radius:5px;" src="/image/card/type/autre-monde.jpg" alt="Autre monde">
                        <img class="responsive-img card-image" style="width: 100px;border-radius:5px;" src="/image/card/type/mythe.jpg" alt="Carte Mythe">
                        <img class="responsive-img card-image" style="width: 100px;border-radius:50%;" src="/image/card/type/PortailBack.jpg" alt="Portail">
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
      pageTitle: 'Mélange des paquets de l\'ancien',
    };
  },
  methods: {
    continueAction() {
      // console.log('ici')
      this.$router.push('place-investigators');
    },
  },
};
</script>

<style>
    img .card-image
    {
        width: 100px;
        display: inline-block;
    }
</style>
