<template>
    <div class="container">

        <h1 class="center-align">{{ pageTitle2 }}</h1>

        <div class="row">

            <div class="col m7">
                <div class="divider"></div>
                <div class="row">
                    <div class="card">
                        <div class="col m12">
                            <blockquote>Le joueur {{ first }} commencera la partie</blockquote>
                        </div>
                        <div class="col m12">
                            <div v-if="!enableSubmit">
                                Le joueur {{ current }} doit choisir son investivateur :
                            </div>
                        </div>
                    </div>
                </div>

                <div class="divider"></div>
                <br>

                <div class="row center-align">
                    <button v-for="player in available"
                        v-bind:class="player.disabled"
                        @click="choose(player)"
                        @mouseover="mouseOver(player.name)"
                        @mouseleave="hovered=''"
                        class="btn">
                        {{ player.name }}
                    </button>
                    <br><br>
                    <button class="btn" :disabled="!enableSubmit" @click="submit">Confirmer</button>
                    <button class="btn" @click="reboot">Réattribuer les personnages</button>
                </div>

                <br>
                <div class="divider"></div>
                <br>

                <div class="row">
                    <!-- Messages récapitulatifs des choix de personnages -->
                    <div v-for="investigator in investigators"
                        class="col m5 character-resume center-align card teal lighten-3"
                        role="alert"
                        @mouseover="mouseOver(investigator.name)"
                        @mouseleave="hovered=''">
                        <div class="card-content">
                            <p>Joueur {{investigator.player}} :<br> {{investigator.name}}</p>
                        </div>
                    </div>
                </div>
                <blockquote v-if="enableSubmit">
                    {{ recapMessage }}
                </blockquote>
            </div>

            <div class="col m5 center-align">
                <transition name="fade">
                    <div v-if="hovered !=''"
                        id="image_content"
                        class="center-align card">
                        <img id="image-preview" :src="imagePath">
                    </div>
                </transition>
            </div>
        </div>

    </div>
</template>

<script>

import axios from 'axios';

export default {
  data() {
    return {
      pageTitle2: 'Choix des investigateurs',
      playerNumber: 6,
      first: 1,
      current: 1,
      enableSubmit: false,
      recapMessage: '',
      hovered: '',
      investigators: [],
      // waitSubmit: true,
      preview: '',
      imagePath: '',
      available: [{
        disabled: '',
        name: 'Joe Diamond',
      },
      {
        disabled: '',
        name: 'Jenny Barnes',
      },
      {
        disabled: '',
        name: 'Mark Harrigan',
      },
      {
        disabled: '',
        name: 'Michael McGlen',
      },
      {
        disabled: '',
        name: 'Peggy Green',
      },
      {
        disabled: '',
        name: 'Francis Sailor',
      },
      ],
    };
  },
  methods: {
    choose(player) {
      if (player.disabled == '') {
        if (this.current <= this.playerNumber) {
          this.investigators.push({
            player: this.current,
            name: player.name,
          });
          player.disabled = 'disabled';
          if (this.current < this.playerNumber) this.current += 1;
          else if (this.current === this.playerNumber) {
            this.allowSubmitButtons();
          }
        }
      }
    },
    // Remise à zero des props pour choisir à nouveau les personnages
    reboot() {
      this.current = 1;
      this.enableSubmit = false;
      this.investigators = [];
      this.available.forEach((character) => {
        character.disabled = '';
      });
    },
    mouseOver(name) {
      this.hovered = true;
      this.imagePath = `/image/sheet/character/${name.replace(' ', '')}.jpg`;
    },
    allowSubmitButtons() {
      this.enableSubmit = true;
      this.available.forEach((character) => {
        character.disabled = 'disabled';
      });
    },
    submit() {
      // Envoi des données au serveur
      // Diriger vers le nouveau composant
      self = this;
      // Requete avec axios pour enregistrer les données
      axios.post('http://127.0.0.1:5000/envoiDonnees/' + 'choose-characters', {
        investigators: this.investigators,
      })
        .then((response) => {
          // Redirige vers le prochain composant
          console.log(response);
          this.$router.push('mix-ally-package');
        })
        .catch((error) => {
          // handle error
          console.log(error);
        })
    },
  },
  updated() {
    this.recapMessage = this.playerNumber == 1 ? 'Le joueur 1 a été choisi. Vous pouvez le réattribuer ou passer à l\'étape suivante.'
      : 'Les joueurs ont été choisis. Vous pouvez les réattribuer ou passer à l\'étape suivante.';
  },
mounted() {
    // vérification de données
    axios.post('http://127.0.0.1:5000/checker/choose-characters', {})
      .then((response) => {
        // récupération du nombre de joueurs et des noms des joueurs si on est deja passé sur cette page
        // console.log(response.data)
        if (response.data.deja === true) {
          var cpt = 1;
          response.data.investigateurs.forEach((inv) => {
            this.investigators.push({ name: inv, player: cpt });
            cpt += 1;
          });
          this.allowSubmitButtons();
        }
        this.playerNumber = response.data.nombreJoueurs;
      });
  },
  computed: {
  },
};
</script>

<style>
    .btn {
        border-radius: 5px;
        margin: 2px;
    }

    .selected {
        border: 3px solid lightgreen;
        -webkit-box-shadow: -3px -2px 5px 0px lightgreen;
        -moz-box-shadow: -3px -2px 5px 0px lightgreen;
        box-shadow: -3px -2px 5px 0px lightgreen;
    }

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

    .character-resume {
        margin: 4px;
    }


    /*TRANSITIONS*/

    .fade-enter-active,
    .fade-leave-active {
        transition: opacity .75s;
    }

    .fade-enter,
    .fade-leave-to {
        opacity: 0;
    }
</style>
