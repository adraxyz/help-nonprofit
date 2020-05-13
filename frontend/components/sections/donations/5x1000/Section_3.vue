<template>
  <section id="fivepermille-section-3" class="padding-level-3">

    <div class="section-title-center text-center">
      <span class="section-title">{{data.title}}</span>
    </div>

    <div class="text-center">
      <div>
        <span class="text-subtitle input-title d-block" v-html="baseText.title"/>
        <input type="number" step="0.01" class="text-center input-text" placeholder="_______"
               v-model="ral" v-on:input="calc5x1000"/>
      </div>
      <div class="text-title result text-center" v-if="five_x_1000">
        <span>{{baseText.subtitle}}</span>
        <span class="result-number">{{five_x_1000}}</span>€
      </div>
      <div class="reward">
        <span class="text-title reward-content" v-html="reward(five_x_1000)"/>
      </div>
    </div>
  </section>
</template>

<script>
  export default {
    name: "Section_3",
    props: {
      data: Object
    },
    data: () => ({
      ranges: [
        {index: 1, ral: 0, coeff: 0.23},
        {index: 2, ral: 15000, coeff: 0.27},
        {index: 3, ral: 28000, coeff: 0.38},
        {index: 4, ral: 55000, coeff: 0.41},
        {index: 5, ral: 75000, coeff: 0.43}
      ],
      ral: '',
      irpef: 0,
      five_x_1000: ''
    }),
    computed: {
      baseText() {
        return this.data.texts.find(t => t.order === 0)
      }
    },
    methods: {
      calc5x1000() {
        this.irpef = 0
        this.five_x_1000 = ''
        if (this.ral > 0) {
          this.ranges.forEach(
            range => this.irpef += (
              range.coeff * Math.max(0, Math.min(this.ral, this.nextRal(range.index)) - range.ral)
            )
          )
          this.five_x_1000 = (this.irpef / 1000 * 5).toFixed(2)
        }
      },
      nextRal(index) {
        let next_ral = this.ranges.find(r => r.index === index + 1)
        if (next_ral) {
          return next_ral.ral
        }
        return Infinity
      },
      reward(donation) {
        let reward_msg = ''
        let texts = this.data.texts.filter(t => t.order > 0)
        let sup = texts.filter(t => parseFloat(t.title) > donation)
        let max = sup.length > 0 ? Math.min.apply(Math, sup.map(function(o) { return parseFloat(o.title); })) : Infinity
        let inf = texts.filter(t => parseFloat(t.title) <= donation)
        let min = inf.length > 0 ? Math.max.apply(Math, inf.map(function(o) { return parseFloat(o.title); })) : 0
        let reward = texts.find(t => parseFloat(t.title) >= min && parseFloat(t.title) < max)
        if (reward) {
          reward_msg = reward.content
        }
        return reward_msg
      }
    }
  }
</script>

<style lang="scss">
  #fivepermille-section-3 {
    margin-bottom: 10vh;
    .section-title {
      margin-bottom: 5vh;
    }
    .input-title {
      margin-right: 1vw;
    }
    .input-text {
      background-color: white;
      border: 2px solid black;
      height: 60px;
      margin-top: 1vh;
      margin-bottom: 2vh;
      font-family: "Crossten Book";
      font-size: 25px;
    }
    .result-number {
      color: $error-color;
    }
    .reward {
      color: $error-color;
      margin-top: 2vh;
      width: 100%;
    }
    .reward-content {
      max-width: 600px;
      display: inline-block;
    }
    /* Chrome, Safari, Edge, Opera */
    input::-webkit-outer-spin-button,
    input::-webkit-inner-spin-button {
      -webkit-appearance: none;
      margin: 0;
    }
    /* Firefox */
    input[type=number] {
      -moz-appearance: textfield;
    }
  }
  @media #{map-get($display-breakpoints, 'sm-and-down')} {
    #fivepermille-section-3 {
      .input-text {
        max-width: calc(100vw - #{$md-down-logo-margin}*2);
        height: 50px;
        font-size: 20px;
      }
      .reward-content {
        max-width: 450px;
      }
      .text-subtitle {
        font-size: $font-size-18;
      }
    }
  }
  @media #{map-get($display-breakpoints, 'xs-only')} {
    #fivepermille-section-3 {
      .reward-content {
        max-width: calc(100vw - #{$circle-icon-size}*2);
      }
    }
  }
</style>
