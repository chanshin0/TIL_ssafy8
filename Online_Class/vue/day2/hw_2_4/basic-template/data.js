const data = [
  {
    id: 1211,
    name: "jony",
    age: 40,
    job: "싸피 강사",
    family: ["와이프", "고양이"],
    skill: {
      client: ["react", "vue", "javascript"],
      server: ["django", "flask", "node.js"],
    },
  },
  {
    id: 1212,
    name: "sylvie",
    age: 24,
    job: "웹툰작가",
    family: ["엄마", "남편"],
    skill: {
      client: [],
      server: [],
    },
  },
];

console.log(data[0].name)
console.log(data[1].job)
console.log(data[0].skill.client[2])
console.log(data[0].skill)
console.log(data[1].family[1])