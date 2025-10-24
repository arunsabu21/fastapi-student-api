// API endpoints
const API_BASE = '';
const STUDENT_API = API_BASE + '/students/';
const COURSE_API = API_BASE + '/courses/';
const ENROLL_API = API_BASE + '/enrollments/';

// Elements
const studentList = document.getElementById('studentList');
const courseList = document.getElementById('courseList');
const enrollmentList = document.getElementById('enrollmentList');

// Load Students
function loadStudents() {
    fetch(STUDENT_API)
    .then(res => res.json())
    .then(data => {
        studentList.innerHTML = '';
        data.forEach(s => {
            const li = document.createElement('li');
            li.textContent = `ID: ${s.id}, ${s.name} - Age: ${s.age}`;
            studentList.appendChild(li);
        });
    });
}

// Load Courses
function loadCourses() {
    fetch(COURSE_API)
    .then(res => res.json())
    .then(data => {
        courseList.innerHTML = '';
        data.forEach(c => {
            const li = document.createElement('li');
            li.textContent = `ID: ${c.id}, ${c.name}`;
            courseList.appendChild(li);
        });
    });
}

// Load Enrollments
function loadEnrollments() {
    fetch(ENROLL_API)
    .then(res => res.json())
    .then(data => {
        enrollmentList.innerHTML = '';
        data.forEach(e => {
            const li = document.createElement('li');
            li.textContent = `${e.student} enrolled in ${e.course}`;
            enrollmentList.appendChild(li);
        });
    });
}

// Initial load
loadStudents();
loadCourses();
loadEnrollments();

// Add Student
document.getElementById('addStudentForm').addEventListener('submit', e => {
    e.preventDefault();
    const name = document.getElementById('studentName').value;
    const age = parseInt(document.getElementById('studentAge').value);
    fetch(STUDENT_API, {
        method: 'POST',
        headers: {'Content-Type':'application/json'},
        body: JSON.stringify({name, age})
    }).then(res => res.json())
      .then(() => { loadStudents(); e.target.reset(); });
});

// Add Course
document.getElementById('addCourseForm').addEventListener('submit', e => {
    e.preventDefault();
    const name = document.getElementById('courseName').value;
    fetch(COURSE_API, {
        method: 'POST',
        headers: {'Content-Type':'application/json'},
        body: JSON.stringify({name})
    }).then(res => res.json())
      .then(() => { loadCourses(); e.target.reset(); });
});

// Enroll Student
document.getElementById('enrollForm').addEventListener('submit', e => {
    e.preventDefault();
    const student_id = parseInt(document.getElementById('enrollStudentId').value);
    const course_id = parseInt(document.getElementById('enrollCourseId').value);
    fetch(ENROLL_API, {
        method: 'PUT',
        headers: {'Content-Type':'application/json'},
        body: JSON.stringify({student_id, course_id})
    }).then(res => res.json())
      .then(() => { loadEnrollments(); e.target.reset(); });
});
