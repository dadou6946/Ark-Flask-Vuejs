<template>
    <div class="container">

        <h1 class="center-align">{{ pageTitle2 }}</h1>
        <div class="divider"></div><br>

        <div class="row">

            <div class="col s2">
                <div v-for="bu of button"
                    v-if="bu.hidden != false"
                    @click="changeCharacter(bu.number)"
                    v-bind:class="current == bu.number ? 'lighten-2':''"
                    class="waves-effect waves-light btn teal">
                    Joueur <span v-html="bu.number"></span>
                    </div>
            </div>

            <div class="col s10 center-align">
                <div class="row">
                    <div v-for="(investigator,index) of investigators"
                        v-if="index+1 == current">
                        <span v-html="investigator.name"></span> (joueur <span v-html="index + 1"></span>) choisit ses capacités :
                        <br><br><br>

                        <!-- textes d'aptitudes -->
                        <div class="col s4 col offset-s1">
                            <div class="skills">
                                <div>vitesse :</div>
                                <div>discretion:</div>
                            </div>
                            <div class="skills">
                                <div>vigueur:</div>
                                <div>volonté:</div>
                            </div>
                            <div class="skills">
                                <div>savoir:</div>
                                <div>chance:</div>
                            </div>
                        </div>

                        <!-- Fleche gauche -->
                        <div class="col s1">
                            <img class="arrows" @click="changeSkills('vidi', 'left')" src="image/icon/chevron-gauche.png">
                            <img class="arrows" @click="changeSkills('vivo', 'left')" src="image/icon/chevron-gauche.png">
                            <img class="arrows" @click="changeSkills('sach', 'left')" src="image/icon/chevron-gauche.png">
                        </div>


                        <!-- valeurs -->
                        <div class="col s4">
                            <div v-for="(skills,index) of investigator.availableSkills" class="row row-skills"
                            >
                                <div v-for="(value) of skills"
                                    class="col s3"
                                    v-html="value"
                                    v-bind:class="investigator.skills[index] == value?globule(index):''"
                                >
                                </div>
                                <br>
                                <div v-if="index =='discretion' || index =='volonte'">
                                    <br><br>
                                </div>

                            </div>
                        </div>

                        <!-- Fleche droite -->
                        <div class="col s1">
                            <img class="arrows" @click="changeSkills('vidi', 'right')" src="image/icon/chevron-droit.png">
                            <img class="arrows" @click="changeSkills('vivo', 'right')" src="image/icon/chevron-droit.png">
                            <img class="arrows" @click="changeSkills('sach', 'right')" src="image/icon/chevron-droit.png">
                        </div>

                        <br>
                    </div>
                </div>


                <div class="divider"></div><br>

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

      pageTitle2: 'Choix des compétences',
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
        {
          name: 'Joe Diamond',
          skills: {
            vitesse: 3, discretion: 4, vigueur: 2, volonte: 3, savoir: 0, chance: 3,
          },
          availableSkills: {
            vitesse: [3, 4, 5, 6], discretion: [4, 3, 2, 1], vigueur: [2, 3, 4, 5], volonte: [3, 2, 1, 0], savoir: [0, 1, 2, 3], chance: [3, 2, 1, 0],
          },
        },
        {
          name: 'Peggy Green',
          skills: {
            vitesse: 1, discretion: 5, vigueur: 1, volonte: 3, savoir: 1, chance: 5,
          },
          availableSkills: {
            vitesse: [1, 2, 3, 4], discretion: [5, 4, 3, 2], vigueur: [1, 2, 3, 4], volonte: [3, 2, 1, 0], savoir: [1, 2, 3, 4], chance: [5, 4, 3, 2],
          },
        },
        {
          name: 'Jenny Barnes',
          skills: {
            vitesse: 0, discretion: 3, vigueur: 2, volonte: 3, savoir: 0, chance: 4,
          },
          availableSkills: {
            vitesse: [0, 1, 2, 3], discretion: [3, 2, 1, 0], vigueur: [2, 3, 4, 5], volonte: [3, 2, 1, 0], savoir: [0, 1, 2, 3], chance: [4, 3, 2, 0],
          },
        },
        {
          name: 'Francis Sailor',
          skills: {
            vitesse: 1, discretion: 4, vigueur: 1, volonte: 3, savoir: 2, chance: 5,
          },
          availableSkills: {
            vitesse: [1, 2, 3, 4], discretion: [4, 3, 2, 1], vigueur: [1, 2, 3, 4], volonte: [3, 2, 1, 0], savoir: [2, 3, 4, 5], chance: [5, 4, 3, 2],
          },
        },
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
    changeSkills(apt, side) {
      const currentInv = this.investigators[(this.current - 1)]; // investigateur actuel

      if (apt == 'vidi') {
        if (side == 'left') {
          // on vérifie sur vitesse -- existe dans les vitesses dispo, idem pour discretion ++
          if (currentInv.availableSkills.vitesse.includes((currentInv.skills.vitesse - 1)) == true && currentInv.availableSkills.discretion.includes((currentInv.skills.discretion + 1)) == true) {
            // si oui, on fait vitesse-- et discression ++
            currentInv.skills.discretion++;
            currentInv.skills.vitesse--;
          }
        } else if (side == 'right') {
          // on vérifie sur vitesse ++ existe dans les vitesses dispo, idem pour discretion --
          if (currentInv.availableSkills.vitesse.includes((currentInv.skills.vitesse + 1)) == true && currentInv.availableSkills.discretion.includes((currentInv.skills.discretion - 1)) == true) {
            // si oui, on fait vitesse++ et discression --
            currentInv.skills.discretion--;
            currentInv.skills.vitesse++;
          }
        }
      } else if (apt == 'vivo') {
        if (side == 'left') {
          // on vérifie sur vigueur -- existe dans les vigueurs dispo, idem pour volonté ++
          if (currentInv.availableSkills.vigueur.includes((currentInv.skills.vigueur - 1)) == true && currentInv.availableSkills.volonte.includes((currentInv.skills.volonte + 1)) == true) {
            // si oui, on fait vigueur-- et discression ++
            currentInv.skills.volonte++;
            currentInv.skills.vigueur--;
          }
        } else if (side == 'right') {
          // on vérifie sur vigueur ++ existe dans les vigueurs dispo, idem pour volonte --
          if (currentInv.availableSkills.vigueur.includes((currentInv.skills.vigueur + 1)) == true && currentInv.availableSkills.volonte.includes((currentInv.skills.volonte - 1)) == true) {
            // si oui, on fait vigueur++ et discression --
            currentInv.skills.volonte--;
            currentInv.skills.vigueur++;
          }
        }
      } else if (apt == 'sach') {
        if (side == 'left') {
          // on vérifie sur savoir -- existe dans les savoirs dispo, idem pour chance ++
          if (currentInv.availableSkills.savoir.includes((currentInv.skills.savoir - 1)) == true && currentInv.availableSkills.chance.includes((currentInv.skills.chance + 1)) == true) {
            // si oui, on fait savoir-- et discression ++
            currentInv.skills.chance++;
            currentInv.skills.savoir--;
          }
        } else if (side == 'right') {
          // on vérifie sur savoir ++ existe dans les savoirs dispo, idem pour chance --
          if (currentInv.availableSkills.savoir.includes((currentInv.skills.savoir + 1)) == true && currentInv.availableSkills.chance.includes((currentInv.skills.chance - 1)) == true) {
            // si oui, on fait savoir++ et discression --
            currentInv.skills.chance--;
            currentInv.skills.savoir++;
          }
        }
      }
    },
    globule(index) {
      switch (index) {
        case 'vitesse': case 'vigueur': case 'savoir':
          return 'glob-top';
        case 'discretion': case 'volonte': case 'chance':
          return 'glob-bot';
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
      // console.log('ici')
      this.$router.push('set-up-monsters');
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
      box-shadow: -3px -2px 5px 0px lightgreen;        }

  .glob-top {
      border: 3px solid;
      border-color: red red transparent red;
      border-radius: 8px 8px 0 0;
  }

  .glob-bot {
      border: 3px solid;
      border-color: transparent blue blue blue;
      border-radius: 0 0 8px 8px;
  }

  .row-skills {
      margin-bottom: 0px !important;
  }
  .skills {
    margin-top: 10px;
    margin-bottom: 45px;
  }
  .arrows {
    margin-top: 5px;
    margin-bottom: 32px;
  }
</style>
