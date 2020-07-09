<template>
    <div class="container">

        <h1 class="center-align">{{ pageTitle2 }}</h1>
        <div class="divider"></div>
        <br>

        <div class="row">

            <div class="col m2">
                <div v-for="bu of button"
                    v-if="bu.hidden != false"
                    @click="changeCharacter(bu.number)"
                    v-bind:class="current == bu.number ? 'lighten-2':''"
                    class="waves-effect waves-light btn teal">
                    Joueur <span v-html="bu.number"></span>
                    </div>
            </div>

            <div class="col m10 center-align">

                <div v-for="(investigator,index) of investigators"
                    v-if="index+1 == current">
                    <p class="center-align">
                        <span v-html="investigator.name"></span> (joueur <span v-html="index + 1"></span>) commence la partie avec :
                    </p>
                    <div class="row">
                        <ul class="list-unstyled list-inline center-align" >
                            <li v-for="ob of investigator.object" class="il-display">
                                <div class="card" style="margin: 5px;">
                                    <div class="card-image">
                                      <img class="responsive-img" style="width:159px;height:245px;padding: 3px;"
                                            :src="'/image/card/common/'+ob.replace(' ','_')+'.jpg'">
                                    </div>
                                    <div class="card-content">
                                      <p v-html="ob"></p>
                                    </div>
                                </div>
                            </li>
                        </ul>
                    </div>
                    <br>
                </div>

                <br>

                <button v-if="current!=4"
                    class="waves-effect waves-light btn teal"
                    @click="nextPlayer">Joueur suivant</button>

                <button v-if="next==true"
                    class="waves-effect waves-light btn teal"
                    @click="continueAction">Etape suivante</button>
            </div>
        </div>

    </div>
</template>

<script>
export default {
  data() {
    return {
      pageTitle2: 'Attribution des possessions fixes',
      playerNumber: 4,
      first: 1,
      current: 1,
      next: false,
      button: [
        { number: 1, hidden: true },
        { number: 2, hidden: false },
        { number: 3, hidden: false },
        { number: 4, hidden: false },
      ],
      investigators: [
        { name: 'Joe Diamond', object: ['Automatique 45'] },
        { name: 'Peggy Green', object: ['Croix', 'Lanterne'] },
        { name: 'Jenny Barnes', object: ['Dynamite', 'Lance-flammes', 'Hache'] },
        { name: 'Francis Sailor', object: ['Manteau sombre', 'Motocyclette'] },
      ],
    };
  },
  methods: {
    // Au click sur bouton jouerur suivant
    nextPlayer() {
      // Si pas dernier joueur
      if (this.current != this.playerNumber) {
        // Incrémentation du joueur actuel
        ++this.current;
        // Apparition du bouton lié au joueur affiché
        this.button[this.current - 1].hidden = true;
        // Affichage du bouton d'étape suivante si l'on est au dernier joueur
        if (this.current == this.playerNumber) {
          this.next = true;
        }
      }
    },
    // changer l'affichage des personnages
    changeCharacter(number) {
      this.current = number;
    },
    log(message) {
      console.log(message);
    },
    continueAction() {
      this.$router.push('mix-investigator-package');
    },


  },
};

</script>

<style>
    .btn
    {
        border-radius: 5px;
        margin: 2px;
    }
    .selected
    {
        border: 3px solid lightgreen;
        -webkit-box-shadow: -3px -2px 5px 0px lightgreen;
        -moz-box-shadow: -3px -2px 5px 0px lightgreen;
        box-shadow: -3px -2px 5px 0px lightgreen;
    }
    div.object-card
    {
        height: 360px;
        margin: 15px;
        /*display: text;*/
    }
    .il-display
    {
        display: inline-block;
    }
    div.card-image-content
    {
        width:159px;height:245px;
    }

    img.object-image-cards
    {
        padding: 3px;margin: 5px;
    }


</style>
