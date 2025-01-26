
const API_URL = "http://127.0.0.1:8000/api/groups/"

const groupList = document.getElementById("groupList")
const scheduleView = document.getElementById("scheduleView")
const scheduleList = document.getElementById("scheduleList")
const backButton = document.getElementById("backButton")

const daysOfWeek = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

async function fetchGroups() {
  try {
    const response = await fetch(API_URL)
    if (!response.ok) {
      throw new Error("Failed to fetch groups")
    }
    const groups = await response.json()
    displayGroups(groups)
  } catch (error) {
    console.error("Error:", error)
    groupList.innerHTML = "<p>Failed to load groups. Please try again later.</p>"
  }
}

function displayGroups(groups) {
  groupList.innerHTML = ""
  groups.forEach((group) => {
    const groupCard = document.createElement("div")
    groupCard.className = "group-card"
    groupCard.innerHTML = `
            <h3>${group.name}</h3>
            <p>Teachers: ${group.teachers.map((t) => `${t.name} ${t.surname}`).join(", ")}</p>
            <p>Lessons: ${group.lessons.length}</p>
        `
    groupCard.addEventListener("click", () => displaySchedule(group))
    groupList.appendChild(groupCard)
  })
}

function displaySchedule(group) {
  groupList.classList.add("hidden")
  scheduleView.classList.remove("hidden")
  scheduleList.innerHTML = ""

  daysOfWeek.forEach((day) => {
    const dayLessons = group.lessons.filter((lesson) => lesson.day === day)
    const daySchedule = document.createElement("div")
    daySchedule.className = `day-schedule ${day === getCurrentDay() ? "current-day" : ""}`
    daySchedule.innerHTML = `<h3>${day}</h3>`

    if (dayLessons.length > 0) {
      dayLessons.forEach((lesson) => {
        const teacher = group.teachers.find((t) => t.group === group.id) || group.teachers[0]
        const lessonCard = document.createElement("div")
        lessonCard.className = "lesson-card"
        lessonCard.innerHTML = `
                    <img src="${teacher.image}" alt="${teacher.name} ${teacher.surname}" class="teacher-image">
                    <div class="lesson-info">
                        <p><strong>${teacher.name} ${teacher.surname}</strong></p>
                        <p>Time: ${lesson.time}</p>
                        <p>Classroom: ${lesson.classroom}</p>
                    </div>
                `
        daySchedule.appendChild(lessonCard)
      })
    } else {
      daySchedule.innerHTML += "<p>No lessons scheduled</p>"
    }

    scheduleList.appendChild(daySchedule)
  })
}

function getCurrentDay() {
  return daysOfWeek[new Date().getDay()]
}

backButton.addEventListener("click", () => {
  scheduleView.classList.add("hidden")
  groupList.classList.remove("hidden")
})

fetchGroups()

