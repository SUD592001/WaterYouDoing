// get CSRF token
const csrfToken = document.getElementsByName('csrfmiddlewaretoken')[0].getAttribute('value');

// Questions Array
const questions = [
    { question: 'On average, how many loads of laundry do you use per week?', name: 'weekly_laundry_loads', type: 'text', pattern: /^[0-9]+$/},
    { question: 'Do you have a top load, or front load washer?', name: 'washer_type'},
    { question: 'On average, how many times do you go to the bathroom each day?', name: 'daily_bathroom_trips', type: 'text', pattern: /^[0-9]+$/},
    { question: 'On average, how many showers do you take in a week?', name: 'weekly_showers', type: 'text', pattern: /^[0-9]+$/},
    { question: 'Do you have a normal, or efficient shower head?', name: 'shower_head'},
    { question: 'On average, how long are your showers? (in minutes)', name: 'shower_times', type: 'text', pattern: /^[0-9]+$/},
    { question: 'On average, how many baths do you take in a week?', name: 'weekly_baths', type: 'text', pattern: /^[0-9]+$/},
    { question: 'On average, how many times do you wash your dishes in a week?', name: 'weekly_dishes', type: 'text', pattern: /^[0-9]+$/},
    { question: 'On average, how many times do you water your lawn in a week?', name: 'weekly_sprinkler', type: 'text', pattern: /^[0-9]+$/},
    { question: 'How big is your swimming pool, if you have one?', name: 'swimming_pool'},
    // { question: 'Enter Your Email', pattern: /\S+@\S+\.\S+/ },
    // { question: 'Create A Password', type: 'password' }
  ];

// Transition Times
const shakeTime = 100; // Shake Transition Time
const switchTime = 200; // Transition Between Questions

// Init Position At First Question
let position = 0;

// Init DOM Elements
const formBox = document.querySelector('#form-box');
const nextBtn = document.querySelector('#next-btn');
const prevBtn = document.querySelector('#prev-btn');
const inputGroup = document.querySelector('#input-group');
const inputField = document.querySelector('#input-field');
const inputLabel = document.querySelector('#input-label');
const inputProgress = document.querySelector('#input-progress');
const progress = document.querySelector('#progress-bar');

// EVENTS

// Get Question On DOM Load
document.addEventListener('DOMContentLoaded', getQuestion);

// Next Button Click
nextBtn.addEventListener('click', validate);

//Previous Button Click
prevBtn.addEventListener('click', goPrevious);

// Input Field Enter Click
inputField.addEventListener('keyup', e => {
  if (e.keyCode == 13) {
    /*if (position == 0 || position == 2 || position == 3 || (position >= 4 && position <=8))
    intValidate();
    else*/ 
    validate();
  }
});

// FUNCTIONS

// Get Question From Array & Add To Markup
function getQuestion() {
  // Get Current Question
  inputLabel.innerHTML = questions[position].question;
  // Get Current Type
  inputField.type = questions[position].type || 'text';
  // Get Current Answer
  inputField.value = questions[position].answer || '';
  // Focus On Element
  inputField.focus();

  // Set Progress Bar Width - Variable to the questions length
  progress.style.width = (position * 100) / questions.length + '%';

  // Add User Icon OR Back Arrow Depending On Question
  prevBtn.className = position ? 'fas fa-arrow-left' : 'fas fa-user';

  showQuestion();
}

// Display Question To User
function showQuestion() {
  inputGroup.style.opacity = 1;
  inputProgress.style.transition = '';
  inputProgress.style.width = '100%';
}

// Hide Question From User
function hideQuestion() {
  inputGroup.style.opacity = 0;
  inputLabel.style.marginLeft = 0;
  inputProgress.style.width = 0;
  inputProgress.style.transition = 'none';
  inputGroup.style.border = null;
}

// Transform To Create Shake Motion
function transform(x, y) {
  formBox.style.transform = `translate(${x}px, ${y}px)`;
}

// Validate int Field
function intValidate() {
  // Make Sure Pattern Matches If There Is One
  if (!inputField.value.match(questions[position].pattern || /.+/)) {
    inputFail();
  } else {
    inputPass();
  }
}

// Validate Field
function validate() {
  // Make Sure Pattern Matches If There Is One
  if (!inputField.value.match(questions[position].pattern)) {
    inputFail();
  } else {
    inputPass();
  }
}

// Field Input Fail
function inputFail() {
  formBox.className = 'error';
  // Repeat Shake Motion -  Set i to number of shakes
  for (let i = 0; i < 6; i++) {
    setTimeout(transform, shakeTime * i, ((i % 2) * 2 - 1) * 20, 0);
    setTimeout(transform, shakeTime * 6, 0, 0);
    inputField.focus();
  }
}

function goPrevious() {
  position --;
  formBox.className = '';
  setTimeout(transform, shakeTime * 0, 0, 10);
  setTimeout(transform, shakeTime * 1, 0, 0);

  if (questions[position]) {
    hideQuestion();
    getQuestion();
  } else {
    // Remove If No More Questions
    hideQuestion();
    formBox.className = 'close';
    progress.style.width = '100%';

    // Form Complete
    formComplete();
  }
}

// Field Input Passed
function inputPass() {
  formBox.className = '';
  setTimeout(transform, shakeTime * 0, 0, 10);
  setTimeout(transform, shakeTime * 1, 0, 0);

  // Store Answer In Array
  questions[position].answer = inputField.value;

  // Increment Position
  position++;

  // If New Question, Hide Current and Get Next
  if (questions[position]) {
    hideQuestion();
    getQuestion();
  } else {
    // Remove If No More Questions
    hideQuestion();
    formBox.className = 'close';
    progress.style.width = '100%';

    // Form Complete
    formComplete();
  }
}

// build POST data string
function buildPOSTData() {
  // include CSRF token
  postData = 'csrfmiddlewaretoken=' + csrfToken + '&';
  for (i = 0; i < questions.length; i++) {
    postData += questions[i].name + '=' + encodeURI(questions[i].answer);
    if (i < questions.length - 1) {
      postData += '&';
    }
  }
  return postData;
}

// All Fields Complete - Show h1 end
function formComplete() {
  // POST to server
  var xhr = new XMLHttpRequest();
  xhr.open("POST", "/evaluate/new/", true);
  xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded; charset=UTF-8");
  console.log(buildPOSTData());
  xhr.send(buildPOSTData());
  const h1 = document.createElement('h1');
  h1.classList.add('end');
  h1.appendChild(
    document.createTextNode(
      `Thanks ${
        questions[0].answer
      }`
    )
  );
  setTimeout(() => {
    formBox.parentElement.appendChild(h1);
    setTimeout(() => (h1.style.opacity = 1), 50);
  }, 1000);
}
