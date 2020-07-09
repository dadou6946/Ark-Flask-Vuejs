<template>
        <body>
            <app-sidebar></app-sidebar>
            <!-- ARKHAM MAP -->
            <app-map
                     :investigators="investigators"
                     :monsters="monsters"
                     :sites="sites"
                     :beyond="beyond"
                     :specials="specials"
                     ></app-map>

            <!-- Modale de simple message -->
            <app-simple-modal :title="modalTexts.title"
                              :content="modalTexts.content"
                              :buttonText="modalTexts.buttonText"
                              :route="modalTexts.route">
            </app-simple-modal>
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
      pageTitle: 'Apparition des indices',
      modalTexts: {
        title: 'Apparition des indices',
        content: "Des indices sont apparus dans les lieux instables d'Arkham.",
        buttonText: 'Etape suivante',
        route: 'set-fixed-objects',
      },
      monsters: [],
      investigators: [],
      sites: [
        {
          name: 'Boutique<br>de<br>souvenir', id: '1', type: 'site', character: [], monster: [], event: [], clue: 1, color: 'orange', portal: [], marker: [], white: 27, black: 27,
        },
        {
          name: 'Journal', id: '2', type: 'site', character: [], monster: [], event: [], clue: 0, color: 'orange', portal: [], marker: [], white: 27, black: 27,
        },
        {
          name: 'Gare', id: '3', type: 'site', character: [], monster: [], event: [], clue: 0, color: 'orange', portal: [], marker: [], white: 27, black: 27,
        },
        {
          name: "Banque<br>d'Arkham", id: '4', type: 'site', character: [], monster: [], event: [], clue: 0, color: 'white', portal: [], marker: [], white: 28, black: 28,
        },
        {
          name: "Asile<br>d'Arkham", id: '5', type: 'site', character: [], monster: [], event: [], clue: 0, color: 'white', portal: [], marker: [], white: 28, black: 28,
        },
        {
          name: "Square de<br>l'indépen-<br>-dance", id: '6', type: 'site', character: [], monster: [], event: [], clue: 1, color: 'white', portal: [], marker: [], white: 28, black: 28,
        },
        {
          name: 'Relais<br>routier<br>de Hibb', id: '7', type: 'site', character: [], monster: [], event: [], clue: 1, color: 'grey', portal: [], marker: [], white: 29, black: 29,
        },
        {
          name: 'Restaurant<br>de Velma', id: '8', type: 'site', character: [], monster: [], event: [], clue: 1, color: 'grey', portal: [], marker: [], white: 29, black: 29,
        },
        {
          name: 'Poste<br>de<br>-police', id: '9', type: 'site', character: [], monster: [], event: [], clue: 1, color: 'grey', portal: [], marker: [], white: 29, black: 29,
        },
        {
          name: "L'ile<br>inexplorée", id: '10', type: 'site', character: [], monster: [], event: [], clue: 1, color: 'green', portal: [], marker: [], white: 30, black: 30,
        },
        {
          name: 'Les<br>quais', id: '11', type: 'site', character: [], monster: [], event: [], clue: 1, color: 'green', portal: [], marker: [], white: 30, black: 30,
        },
        {
          name: "l'Inno-<br>-mable", id: '12', type: 'site', character: [], monster: [], event: [], clue: 1, color: 'green', portal: [], marker: [], white: 30, black: 30,
        },
        {
          name: 'Le<br>cimetière', id: '13', type: 'site', character: [], monster: [], event: [], clue: 1, color: 'purple', portal: [], marker: [], white: 31, black: 31,
        },
        {
          name: 'La Caverne<br>noire', id: '14', type: 'site', character: [], monster: [], event: [], clue: 1, color: 'purple', portal: [], marker: [], white: 31, black: 31,
        },
        {
          name: 'Le<br>magasin', id: '15', type: 'site', character: [], monster: [], event: [], clue: 0, color: 'purple', portal: [], marker: [], white: 31, black: 31,
        },
        {
          name: 'Département<br>Scientifique', id: '16', type: 'site', character: [], monster: [], event: [], clue: 1, color: 'yellow', portal: [], marker: [], white: 32, black: 32,
        },
        {
          name: 'Adminis-<br>-tration', id: '17', type: 'site', character: [], monster: [], event: [], clue: 0, color: 'yellow', portal: [], marker: [], white: 32, black: 32,
        },
        {
          name: 'Biblio-<br>-thèque', id: '18', type: 'site', character: [], monster: [], event: [], clue: 0, color: 'yellow', portal: [], marker: [], white: 32, black: 32,
        },
        {
          name: 'Maison<br>de la<br>sorcière', id: '19', type: 'site', character: [], monster: [], event: [], clue: 1, color: 'blue', portal: [], marker: [], white: 33, black: 33,
        },
        {
          name: "Loge du<br>crépuscule<br>d'argent", id: '20', type: 'site', character: [], monster: [], event: [], clue: 1, color: 'blue', portal: [], marker: [], white: 33, black: 33,
        },
        {
          name: 'Hôpital<br>Sainte<br>Marie', id: '21', type: 'site', character: [], monster: [], event: [], clue: 0, color: 'red', portal: [], marker: [], white: 34, black: 34,
        },
        {
          name: 'Vieille<br>échoppe<br>de magie', id: '22', type: 'site', character: [], monster: [], event: [], clue: 0, color: 'red', portal: [], marker: [], white: 34, black: 34,
        },
        {
          name: 'Les<br>bois', id: '23', type: 'site', character: [], monster: [], event: [], clue: 1, color: 'red', portal: [], marker: [], white: 34, black: 34,
        },
        {
          name: 'Pension<br>de Ma', id: '24', type: 'site', character: [], monster: [], event: [], clue: 0, color: 'brown', portal: [], marker: [], white: 35, black: 35,
        },
        {
          name: 'Société<br>des<br>historiens', id: '25', type: 'site', character: [], monster: [], event: [], clue: 1, color: 'brown', portal: [], marker: [], white: 35, black: 35,
        },
        {
          name: 'Eglise<br>méridionale', id: '26', type: 'site', character: [], monster: [], event: [], clue: 0, color: 'brown', portal: [], marker: [], white: 35, black: 35,
        },
        {
          name: 'Quartier<br>Nord', id: '27', type: 'street', character: [], monster: [], event: [], clue: 0, color: 'orange', portal: [], marker: [], white: 28, black: 30,
        },
        {
          name: 'Centre<br>Ville', id: '28', type: 'street', character: [], monster: [], event: [], clue: 0, color: 'white', portal: [], marker: [], white: 29, black: 27,
        },
        {
          name: 'Quartier<br>Est', id: '29', type: 'street', character: [], monster: [], event: [], clue: 0, color: 'grey', portal: [], marker: [], white: 31, black: 28,
        },
        {
          name: 'Quartier<br>marchand', id: '30', type: 'street', character: [], monster: [], event: [], clue: 0, color: 'green', portal: [], marker: [], white: 27, black: 32,
        },
        {
          name: 'Quartier<br>de la<br>rivière', id: '31', type: 'street', character: [], monster: [], event: [], clue: 0, color: 'purple', portal: [], marker: [], white: 33, black: 29,
        },
        {
          name: 'Université<br>Miskatonik', id: '32', type: 'street', character: [], monster: [], event: [], clue: 0, color: 'yellow', portal: [], marker: [], white: 30, black: 34,
        },
        {
          name: 'French<br>Hill', id: '33', type: 'street', character: [], monster: [], event: [], clue: 0, color: 'blue', portal: [], marker: [], white: 35, black: 31,
        },
        {
          name: 'Quartier<br>Résidentiel', id: '34', type: 'street', character: [], monster: [], event: [], clue: 0, color: 'red', portal: [], marker: [], white: 32, black: 35,
        },
        {
          name: 'Quartier<br>sud', id: '35', type: 'street', character: [], monster: [], event: [], clue: 0, color: 'brown', portal: [], marker: [], white: 34, black: 33,
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
        { name: 'Perdu dans<br>le temps<br>et l\'espace', id: 36, character: [] },
        { name: 'Ciel', id: 37, monster: [] },
        { name: 'Périphérie', id: 38, monster: [] },
        { name: 'Cellule de prison', id: 39, monster: [] },
      ],
    };
  },
  methods: {
    log(name) {
      console.log(name);
    },
  },
  updated() {

  },
};
</script>

<style>

</style>
