<template>
  <div class="border">
    <h1>이거는 내가 새로 만든 컴포넌트다</h1>
    <MyComponentItem
      static-props="스태틱 프롭스"    
      :dynamic-props="dynamicProps"
      @child-to-parent="parentGetEvent"
    />
    <!-- =과 :의 차이 -->

  </div>
</template>

<script>
  // 1. 불러오기
  import MyComponentItem from '@/components/MyComponentItem'

  export default {
    name : 'MyComponent',
    // 2. 등록하기
    components:{
      MyComponentItem,
    },
    data:function(){
      return {
        dynamicProps:'이건 동적 데이터다!',
      }
    },
    methods:{
      parentGetEvent:function (childData) {
        console.log('자식 컴포넌트에서 발생한 emit 이벤트를 들어서 이 메소드가 실행된다')
        console.log(childData)
      }
    }
  }
</script>

<style>
  .border {
    border: solid ipx black;
  }
</style>
