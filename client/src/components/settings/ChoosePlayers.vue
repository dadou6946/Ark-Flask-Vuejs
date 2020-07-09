<template>
    <div class="container">

        <h1 class="center-align">{{ pageTitle }}</h1>
        <div class="divider"></div><br>

        <div class="row">
            <div class="col m3">
                <div class="center-align">
                  <label for="">Nombre de joueurs</label>
                  <div>
                    <div class="btn" @click="down" :disabled="playerNumber==1">-</div>
                    <div class="btn">{{playerNumber}}</div>
                    <div class="btn" @click="up" :disabled="playerNumber>5">+</div>
                  </div>
                </div>

                <br><div class="divider"></div>
            </div>

            <div class="col m9">

                <div class="center-align">
                  <div v-for="(player, index) of players">
                    <label>Joueur {{index + 1}}</label>
                    <input type="text" v-model="player.name">
                  </div>
                </div>

                <input type="submit" class="btn" @click="submit" :disabled="!allowConfirm" value="Confirmer">

            </div>

        </div>

        <a @click="test1" class="btn">Test 1</a>

    </div>
</template>

<script>

import axios from 'axios';

export default {
  data() {
    return {
      pageTitle: 'Choix des joueurs',
      playerNumber: 1,
      allowConfirm: false,
      players: [
        {
          name: '',
        },
      ],
      keptData: '',
    };
  },
  methods: {
    up() {
      if (this.playerNumber < 6) {
        this.playerNumber++;
        this.players.push({ name: '' });
        this.allowConfirm = false;
      }
    },
    down() {
      if (this.playerNumber != 1) {
        this.playerNumber--;
        this.players.splice(this.playerNumber, 1);
      }
    },
    test1() {
      axios.get('http://127.0.0.1:5000/test1')
        .then((response) => {
          console.log(response.data)
        });
    },
    submit() {
      // Envoi des données au serveur
      // Diriger vers le nouveau composant
      self = this;
      // Exemple de requete avec axios
      axios.get('https://api.themoviedb.org/3/movie/550?api_key=cbf431d660a6bb41316b07a07bbd9da6')
        .then((response) => {
          // handle success
          self.keptData = response.data.original_title;
          console.log(self.keptData);
          // Redirige vers home ou prochain composant
          self.$router.push('/choose-characters');
        })
        .catch((error) => {
          // handle error
          console.log(error);
        })
        .then(() => {
          // always executed
        });
    },


  },
  updated() {
    let cpt = 0;
    this.players.forEach((player) => {
      if (player.name == '') cpt++;
    });
    if (cpt == 0) this.allowConfirm = true;
  },
  mounted() {
    axios.get('http://127.0.0.1:5000/check/'+ 'choose-players')
        .then((response) => {
          console.log(response.data)
        });
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

</style>
