<template>
    <body>
        <app-sidebar></app-sidebar>

        <!-- ARKHAM MAP -->
        <app-map :investigators="investigators"
                 :sites="sites"
                 :beyond="beyond"
                 :specials="specials"
                 :monsters="monsters"
                 :moves="moves"
                 @wasClicked="move($event)"></app-map>

        <div id="modal-movement-1" class="modal" tabindex="0">
                <div class="modal-content" style="height:100%">
                    <div class="row">
                        <div class="col s12">
                            <h5>Phase de mouvement</h5>
                            <span>Les investigateurs peuvent se déplacer en fonction de leur <b>vitesse</b>, le premier joueur commence:</span><br>
                            <transition name="fade" mode="out-in">
                                <div v-for="investigator of investigators"
                                    v-if="investigator.id == currentPlayer"
                                    :key="investigator.name">
                                    <span>{{ investigator.name }}</span>
                                    <span>Mouvement: {{ investigator.skills.vitesse }}</span>
                                </div>
                            </transition>

                            <span class="btn-small">Confirmer</span>
                            <span class="btn-small">Annuler</span>
                            <span class="btn-small" @click="currentPlayer++">Joueur suivant</span>

                            <hr>
                            <div class="right-align">
                                <div class="btn teal" @click="test">test</div>
                                <button class="waves-effect waves-light btn teal" @click="nextStep">Phase de rencontres à Arkham</button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
    </body>
</template>

<script>
import Sidebar from '../Sidebar.vue';
import SimpleModal from '../SimpleModal.vue';
import Map from '../Map.vue';

export default {
  // déclaration des composants utilisés
  components: {
    'app-sidebar': Sidebar,
    'app-simple-modal': SimpleModal,
    'app-map': Map,
  },
  data() {
    return {
      pageTitle: 'Phase de mouvement',
      playerNumber: 2, // nombre de joueurs
      currentPlayer: 1,
      availableSites: [],
      investigators: [
        {
          id: 1,
          name: 'Joe Diamond',
          siteId: 3,
          status: 'ok',
          skills: {
            vitesse: 3, discretion: 4, vigueur: 2, volonte: 3, savoir: 0, chance: 3,
          },
          availableSkills: {
            vitesse: [3, 4, 5, 6], discretion: [4, 3, 2, 1], vigueur: [2, 3, 4, 5], volonte: [3, 2, 1, 0], savoir: [0, 1, 2, 3], chance: [3, 2, 1, 0],
          },
        },
        {
          id: 2,
          name: 'Peggy Green',
          siteId: 8,
          status: 'lost',
          skills: {
            vitesse: 1, discretion: 5, vigueur: 1, volonte: 3, savoir: 1, chance: 5,
          },
          availableSkills: {
            vitesse: [1, 2, 3, 4], discretion: [5, 4, 3, 2], vigueur: [1, 2, 3, 4], volonte: [3, 2, 1, 0], savoir: [1, 2, 3, 4], chance: [5, 4, 3, 2],
          },
        },
        {
          id: 3,
          name: 'Jenny Barnes',
          siteId: 9,
          status: 'arrested',
          skills: {
            vitesse: 0, discretion: 3, vigueur: 2, volonte: 3, savoir: 0, chance: 4,
          },
          availableSkills: {
            vitesse: [0, 1, 2, 3], discretion: [3, 2, 1, 0], vigueur: [2, 3, 4, 5], volonte: [3, 2, 1, 0], savoir: [0, 1, 2, 3], chance: [4, 3, 2, 0],
          },
        },
        {
          id: 4,
          name: 'Francis Sailor',
          siteId: 6,
          status: 'retarded',
          skills: {
            vitesse: 1, discretion: 4, vigueur: 1, volonte: 3, savoir: 2, chance: 5,
          },
          availableSkills: {
            vitesse: [1, 2, 3, 4], discretion: [4, 3, 2, 1], vigueur: [1, 2, 3, 4], volonte: [3, 2, 1, 0], savoir: [2, 3, 4, 5], chance: [5, 4, 3, 2],
          },
        },
        {
          id: 5,
          name: 'Mark Harrigan',
          siteId: 7,
          status: 'lost',
          skills: {
            vitesse: 1, discretion: 4, vigueur: 1, volonte: 3, savoir: 2, chance: 5,
          },
          availableSkills: {
            vitesse: [1, 2, 3, 4], discretion: [4, 3, 2, 1], vigueur: [1, 2, 3, 4], volonte: [3, 2, 1, 0], savoir: [2, 3, 4, 5], chance: [5, 4, 3, 2],
          },
        },
      ],
      monsters: [
        {
          id: 1, name: 'Chthonien', siteId: 11, symbol: 'triangle', habilities: {},
        },
        {
          id: 2, name: 'Migo', siteId: 1, symbol: 'cercle', habilities: {},
        },
        {
          id: 3, name: 'Cultiste', siteId: 3, symbol: 'lune', habilities: {},
        },
      ],
      sites: [
        {
          name: 'Boutique<br>de<br>souvenir', id: '1', type: 'site', adjacentSites: [27], character: [], monster: [], event: [], clue: 1, color: 'orange', portal: [], marker: [], white: 27, black: 27,
        },
        {
          name: 'Journal', id: '2', type: 'site', adjacentSites: [27], character: [], monster: [], event: [], clue: 0, color: 'orange', portal: [], marker: [], white: 27, black: 27,
        },
        {
          name: 'Gare', id: '3', type: 'site', adjacentSites: [27], character: [], monster: [], event: [], clue: 0, color: 'orange', portal: [], marker: [], white: 27, black: 27,
        },
        {
          name: "Banque<br>d'Arkham", id: '4', type: 'site', adjacentSites: [28], character: [], monster: [], event: [], clue: 0, color: 'white', portal: [], marker: [], white: 28, black: 28,
        },
        {
          name: "Asile<br>d'Arkham", id: '5', type: 'site', adjacentSites: [28], character: [], monster: [], event: [], clue: 0, color: 'white', portal: [], marker: [], white: 28, black: 28,
        },
        {
          name: "Square de<br>l'indépen-<br>-dance", id: '6', type: 'site', adjacentSites: [28], character: [], monster: [], event: [], clue: 1, color: 'white', portal: [], marker: [], white: 28, black: 28,
        },
        {
          name: 'Relais<br>routier<br>de Hibb', id: '7', type: 'site', adjacentSites: [29], character: [], monster: [], event: [], clue: 1, color: 'grey', portal: [], marker: [], white: 29, black: 29,
        },
        {
          name: 'Restaurant<br>de Velma', id: '8', type: 'site', adjacentSites: [29], character: [], monster: [], event: [], clue: 1, color: 'grey', portal: [], marker: [], white: 29, black: 29,
        },
        {
          name: 'Poste<br>de<br>police', id: '9', type: 'site', adjacentSites: [29], character: [], monster: [], event: [], clue: 1, color: 'grey', portal: [], marker: [], white: 29, black: 29,
        },
        {
          name: "L'ile<br>inexplorée", id: '10', type: 'site', adjacentSites: [30], character: [], monster: [], event: [], clue: 1, color: 'green', portal: [], marker: [], white: 30, black: 30,
        },
        {
          name: 'Les<br>quais', id: '11', type: 'site', adjacentSites: [30], character: [], monster: [], event: [], clue: 1, color: 'green', portal: [], marker: [], white: 30, black: 30,
        },
        {
          name: "l'Inno-<br>-mable", id: '12', type: 'site', adjacentSites: [30], character: [], monster: [], event: [], clue: 1, color: 'green', portal: [], marker: [], white: 30, black: 30,
        },
        {
          name: 'Le<br>cimetière', id: '13', type: 'site', adjacentSites: [31], character: [], monster: [], event: [], clue: 1, color: 'purple', portal: [], marker: [], white: 31, black: 31,
        },
        {
          name: 'La Caverne<br>noire', id: '14', type: 'site', adjacentSites: [31], character: [], monster: [], event: [], clue: 1, color: 'purple', portal: [], marker: [], white: 31, black: 31,
        },
        {
          name: 'Le<br>magasin', id: '15', type: 'site', adjacentSites: [31], character: [], monster: [], event: [], clue: 0, color: 'purple', portal: [], marker: [], white: 31, black: 31,
        },
        {
          name: 'Département<br>Scientifique', id: '16', type: 'site', adjacentSites: [32], character: [], monster: [], event: [], clue: 1, color: 'yellow', portal: [], marker: [], white: 32, black: 32,
        },
        {
          name: 'Adminis-<br>-tration', id: '17', type: 'site', adjacentSites: [32], character: [], monster: [], event: [], clue: 0, color: 'yellow', portal: [], marker: [], white: 32, black: 32,
        },
        {
          name: 'Biblio-<br>-thèque', id: '18', type: 'site', adjacentSites: [32], character: [], monster: [], event: [], clue: 0, color: 'yellow', portal: [], marker: [], white: 32, black: 32,
        },
        {
          name: 'Maison<br>de la<br>sorcière', id: '19', type: 'site', adjacentSites: [33], character: [], monster: [], event: [], clue: 1, color: 'blue', portal: [], marker: [], white: 33, black: 33,
        },
        {
          name: "Loge du<br>crépuscule<br>d'argent", id: '20', type: 'site', adjacentSites: [33], character: [], monster: [], event: [], clue: 1, color: 'blue', portal: [], marker: [], white: 33, black: 33,
        },
        {
          name: 'Hôpital<br>Sainte<br>Marie', id: '21', type: 'site', adjacentSites: [34], character: [], monster: [], event: [], clue: 0, color: 'red', portal: [], marker: [], white: 34, black: 34,
        },
        {
          name: 'Vieille<br>échoppe<br>de magie', id: '22', type: 'site', adjacentSites: [34], character: [], monster: [], event: [], clue: 0, color: 'red', portal: [], marker: [], white: 34, black: 34,
        },
        {
          name: 'Les<br>bois', id: '23', type: 'site', adjacentSites: [34], character: [], monster: [], event: [], clue: 1, color: 'red', portal: [], marker: [], white: 34, black: 34,
        },
        {
          name: 'Pension<br>de Ma', id: '24', type: 'site', adjacentSites: [35], character: [], monster: [], event: [], clue: 0, color: 'brown', portal: [], marker: [], white: 35, black: 35,
        },
        {
          name: 'Société<br>des<br>historiens', id: '25', type: 'site', adjacentSites: [35], character: [], monster: [], event: [], clue: 1, color: 'brown', portal: [], marker: [], white: 35, black: 35,
        },
        {
          name: 'Eglise<br>méridionale', id: '26', type: 'site', adjacentSites: [35], character: [], monster: [], event: [], clue: 0, color: 'brown', portal: [], marker: [], white: 35, black: 35,
        },
        /* 'Migo' */ {
          name: 'Quartier<br>Nord', id: '27', type: 'street', adjacentSites: [1, 2, 3, 28, 30], character: [], monster: [], event: [], clue: 0, color: 'orange', portal: [], marker: [], white: 28, black: 30,
        },
        /* 'Cultiste' */ {
          name: 'Centre<br>Ville', id: '28', type: 'street', adjacentSites: [4, 5, 6, 27, 29], character: [], monster: [], event: [], clue: 0, color: 'white', portal: [], marker: [], white: 29, black: 27,
        },
        {
          name: 'Quartier<br>Est', id: '29', type: 'street', adjacentSites: [7, 8, 9, 28, 31], character: [], monster: [], event: [], clue: 0, color: 'grey', portal: [], marker: [], white: 31, black: 28,
        },
        {
          name: 'Quartier<br>marchand', id: '30', type: 'street', adjacentSites: [10, 11, 12, 27, 28, 31, 32], character: [], monster: [], event: [], clue: 0, color: 'green', portal: [], marker: [], white: 27, black: 32,
        },
        {
          name: 'Quartier<br>de la<br>rivière', id: '31', type: 'street', adjacentSites: [13, 14, 15, 29, 30, 33], character: [], monster: [], event: [], clue: 0, color: 'purple', portal: [], marker: [], white: 33, black: 29,
        },
        {
          name: 'Université<br>Miskatonik', id: '32', type: 'street', adjacentSites: [16, 17, 18, 30, 33, 34], character: [], monster: [], event: [], clue: 0, color: 'yellow', portal: [], marker: [], white: 30, black: 34,
        },
        {
          name: 'French<br>Hill', id: '33', type: 'street', adjacentSites: [19, 20, 31, 32, 35], character: [], monster: [], event: [], clue: 0, color: 'blue', portal: [], marker: [], white: 35, black: 31,
        },
        {
          name: 'Quartier<br>Résidentiel', id: '34', type: 'street', adjacentSites: [21, 22, 23, 32, 35], character: [], monster: [], event: [], clue: 0, color: 'red', portal: [], marker: [], white: 32, black: 35,
        },
        {
          name: 'Quartier<br>sud', id: '35', type: 'street', adjacentSites: [24, 25, 26, 33, 34], character: [], monster: [], event: [], clue: 0, color: 'brown', portal: [], marker: [], white: 34, black: 33,
        },

      ],
      beyond: [
        {
          name: 'Une autre<br>dimension',
          colors: [],
          steps: [
            {
              id: 1, position: 1, character: [], monster: [],
            },
            {
              id: 2, position: 2, character: [], monster: [],
            },
          ],
        },
        {
          name: 'Les Abysses',
          colors: [],
          steps: [
            {
              id: 3, position: 1, character: [], monster: [],
            },
            {
              id: 4, position: 2, character: [], monster: [],
            },
          ],
        },
        {
          name: 'Cité de la<br>Grand Race',
          colors: [],
          steps: [
            {
              id: 5, position: 1, character: [], monster: [],
            },
            {
              id: 6, position: 2, character: [], monster: [],
            },
          ],
        },
        {
          name: 'Yuggoth',
          colors: [],
          steps: [
            {
              id: 7, position: 1, character: [], monster: [],
            },
            {
              id: 8, position: 2, character: [], monster: [],
            },
          ],
        },
        {
          name: 'Grand Hall<br>de Celeano',
          colors: [],
          steps: [
            {
              id: 9, position: 1, character: [], monster: [],
            },
            {
              id: 10, position: 2, character: [], monster: [],
            },
          ],
        },
        {
          name: 'Les contrées<br>du rêve',
          colors: [],
          steps: [
            {
              id: 11, position: 1, character: [], monster: [],
            },
            {
              id: 12, position: 2, character: [], monster: [],
            },
          ],
        },
        {
          name: 'Plateau<br>de Leng',
          colors: [],
          steps: [
            {
              id: 13, position: 1, character: [], monster: [],
            },
            {
              id: 14, position: 2, character: [], monster: [],
            },
          ],
        },
        {
          name: 'R\'lyeh',
          colors: [],
          steps: [
            {
              id: 15, position: 1, character: [], monster: [],
            },
            {
              id: 16, position: 2, character: [], monster: [],
            },
          ],
        },
      ],
      specials: [
        { name: 'Perdu dans<br>le temps<br>et l\'espace', id: 36, character: [{ id: 2, name: 'Francis Sailor' }, { id: 5, name: 'Mark Harrigan' }] },
        { name: 'Ciel', id: 37, monster: [] },
        { name: 'Périphérie', id: 38, monster: [] },
        { name: 'Cellule de prison', id: 39, monster: [] },
      ],
      moves:
                {
                  1: {
                    1: [27],
                    2: [1, 2, 28, 30],
                    3: [10, 11, 12, 4, 5, 6, 29, 32, 31],
                  },
                  2: {
                    1: [29],
                    2: [7, 9, 28, 31],
                    3: [4, 5, 6, 27, 30, 13, 14, 15, 33],
                  },
                  3: {
                    1: [29],
                    2: [7, 8, 28, 31],
                    3: [4, 5, 6, 27, 30, 13, 14, 15, 33],
                  },
                  4: {
                    1: [28],
                    2: [4, 5, 27, 29, 30],
                    3: [1, 2, 3, 7, 8, 9, 10, 11, 12, 32, 31],
                  },
                  5: {
                    1: [29],
                    2: [8, 9, 28, 31],
                    3: [4, 5, 6, 27, 30, 13, 14, 15, 33],
                  },
                },
      // adjacentSites: [
      //     { id: 1 , adjacentSites: [27]},
      //     { id: 2 , adjacentSites: [27]},
      //     { id: 3 , adjacentSites: [27]},
      //     { id: 4 , adjacentSites: [28]},
      //     { id: 5 , adjacentSites: [28]},
      //     { id: 6 , adjacentSites: [28]},
      //     { id: 7 , adjacentSites: [29]},
      //     { id: 8 , adjacentSites: [29]},
      //     { id: 9 , adjacentSites: [29]},
      //     { id: 10, adjacentSites: [30]},
      //     { id: 11, adjacentSites: [30]},
      //     { id: 12, adjacentSites: [30]},
      //     { id: 13, adjacentSites: [31]},
      //     { id: 14, adjacentSites: [31]},
      //     { id: 15, adjacentSites: [31]},
      //     { id: 16, adjacentSites: [32]},
      //     { id: 17, adjacentSites: [32]},
      //     { id: 18, adjacentSites: [32]},
      //     { id: 19, adjacentSites: [33]},
      //     { id: 20, adjacentSites: [33]},
      //     { id: 21, adjacentSites: [34]},
      //     { id: 22, adjacentSites: [34]},
      //     { id: 23, adjacentSites: [34]},
      //     { id: 24, adjacentSites: [35]},
      //     { id: 25, adjacentSites: [35]},
      //     { id: 26, adjacentSites: [35]}, //fin des lieux
      //     { id: 27, adjacentSites: [1,2,3,28,30]},
      //     { id: 28, adjacentSites: [4,5,6,27,29]},
      //     { id: 29, adjacentSites: [7,8,9,28,31]},
      //     { id: 30, adjacentSites: [10,11,12,27,28,31,32]},
      //     { id: 31, adjacentSites: [13,14,15,29,30,33]},
      //     { id: 32, adjacentSites: [16,17,18,30,33,34]},
      //     { id: 33, adjacentSites: [19,20,31,32,35]},
      //     { id: 34, adjacentSites: [21,22,23,32,35]},
      //     { id: 35, adjacentSites: [24,25,26,33,34]}
      // ]

    };
  },
  methods: {

    test() {
      this.log(this.getAvailableSites(17, 4));
    },
    // Récupération des lieux adjacents à celui dont l'id est spécifié
    getAdjacentSites(id) {
      // Recherche le lieu avec l'id en paramètre
      const adjacentSite = this.sites.find(site => site.id == id);
      // Retourne les lieux adjacents
      return adjacentSite.adjacentSites;
    },
    // Retourne les lieux à la distance speed du lieu numéro id
    getAvailableSites(id, speed) {
      // on définit les variables
      const getAvailableSites = [];
      const find = [];
      let last = [];
      // pour chaque point de mouvement
      for (let i = 0; i < speed; i++) {
        // si premier point de mouvement
        if (i == 0) {
          // Recherche des lieux adjacents
          const adjacentSites = this.getAdjacentSites(id);
          // Sauvegarde de l'objet à retourner
          getAvailableSites.push({ rang: 1, sites: adjacentSites });
          // getAvailableSites.push({ rang: 1, sites: adjacentSites });
          // Sauvegarde des lieux trouvés
          adjacentSites.forEach((adj) => {
            find.push(adj);
          });
          // Sauvegarde des derniers lieux trouvés
          last = adjacentSites;
        }
        // Si points de mouvement suivants
        else {
          // Création de l'objet à mettre dans ce qu'on retourne
          var result = { rang: (i + 1), sites: [] };
          // Pour chacun des derniers sites trouvés
          last.forEach((element) => {
            // Recherche des lieux adjacents
            const adj = this.getAdjacentSites(element);
            // Pour chacun de ces lieux trouvés
            adj.forEach((site) => {
              // Si pas encore trouvé et si pas le lieu de départ
              // Ajout au tableau des lieux trouvés et dans l'objet à retourner
              if (find.indexOf(site) == -1 && site != id) {
                find.push(site);
                result.sites.push(site);
              }
            });
          });
          // Sauvegarde de l'objet à retourner
          getAvailableSites.push(result);
          // Sauvegarde des derniers lieux trouvés
          last = result.sites;
        }
      }
      return getAvailableSites;
    },
    move(site) {
      const currentInvestigator = this.getInvestigator(this.currentPlayer);
      const availableSites = this.getAvailableSites(currentInvestigator.siteId, currentInvestigator.skills.vitesse);
    },
    // Récupère l'investigateur dont l'id est passé en paramètre
    getInvestigator(id) {
      return this.investigators.find(investigator => investigator.id == id);
    },
    log(message) {
      console.log(message);
    },

    nextStep() {
      // console.log('ici');
      this.$router.push('arkham-encounter-step');
    },
  },
  updated() {

  },
  mounted() {
    const currentInvestigator = this.getInvestigator(this.currentPlayer);
    this.availableSites = this.getAvailableSites(currentInvestigator.siteId, currentInvestigator.skills.vitesse);
  },
};
</script>

<style>

    /*Modales*/
    #modal-movement-1
    {
        z-index: 999;
        display: block;
        opacity: 1;
        top: 5%;
        width: 20%;
        margin-left: 25px;
        height: 550px;
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
