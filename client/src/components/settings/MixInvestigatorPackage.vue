<template>

    <div class="container">

        <h1 class="center-align">{{ pageTitle }}</h1>

        <div class="divider"></div>

        <div class="row center-align">
            <div class="col-md-12">

                <div>
                    <p>Les paquets investigateur sont mélangés.</p>
                </div>

                <div class="row">
                    <div class="col-md-12">
                        <div class="row center-align">
                            <img class="object-image" src="/image/card/type/ally.jpg" alt="Alliés">
                            <img class="object-image" src="/image/card/type/spell.jpg" alt="Sorts">
                            <img class="object-image" src="/image/card/type/common.jpg" alt="Objets communs">
                            <img class="object-image" src="/image/card/type/unique.jpg" alt="Objets uniques">
                            <img class="object-image" src="/image/card/type/skill.jpg" alt="Compétences">
                        </div>
                    </div>
                </div>

                <div class="divider"></div>
                <br>
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
      pageTitle: 'Mélange des paquets investigateur',
    };
  },
  methods: {
    continueAction() {
      // console.log('ici')
      this.$router.push('set-random-objects');
    },
  },
};
</script>

<style>
    img.object-image
    {
        display: inline-block;
    }
</style>
