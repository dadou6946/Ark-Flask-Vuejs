import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    name: 'Sylvain',
    count: 0,
  },
  mutations: {
    increment(state) {
      // mutate state
      state.count++;
    },
  },
  getters: {
    upperName: state => state.name.toUpperCase(),
  },
  actions: {},
});
