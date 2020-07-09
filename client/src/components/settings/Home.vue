<template>
    <div class="container">

        <h1 class="center-align">{{ pageTitle }}</h1>
        <div class="divider"></div><br>

        <div class="row">
            <div class="col-md-12">

                <div class="center-align">
                  <router-link :to="{ path: '/choose-players' }" class="waves-effect waves-light btn">Nouvelle partie</router-link>
                  <div class="waves-effect waves-light btn" disabled>Continuer une partie</div>
                </div>

                <div>
                  <!-- Boutons de test de methodes -->
                  <a @click="test1" class="btn">Test 1</a>
                  <a @click="test2" class="btn">Test 2</a>
                </div>

            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      pageTitle: 'Accueil',
    };
  },
  methods: {
    // methodes de test
    test1() {
      axios.get('http://127.0.0.1:5000/test1')
        .then((response) => {
          console.log(response.data)
        });
    },
    test2() {
      axios.get('http://127.0.0.1:5000/test2')
        .then((response) => {
          console.log(response.data)
        });
    },
  }
};
</script>
