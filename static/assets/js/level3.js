window.onload = () => {
    let resetButton = document.getElementById('resetButton');
    let submitButton = document.getElementById('submitButton');
    let reviewButton = document.getElementById('reviewButton');

    let whichQuestionsCorrect = [];

    let htmlForTableGenerator = (columns, tableData, questionDOMValue) => {
        var html = "<br><h5><strong>Your table generated from your query: </strong>" + questionDOMValue  +"</h5>";
        html += '<table class="table" id="user-table1"><thead><tr>';
        html += '<th scope="col">#</th>';
        for (var i = 0; i < columns.length; i++) {
            html += '<th scope="col">' + columns[i] + '</th>';
        }
        html += '</tr></thead><tbody>';
        for (var j = 0; j < tableData.length; j++) {
            html += '<tr>';
            html += '<th scope="row">' + (j+1).toString() + '</th>'
            for (var k = 0; k < tableData[j].length; k++) {
                html += '<td>' + tableData[j][k] + '</td>';
            }
            html += '</tr>';
        }
        html += '</table>';
        return html;
    }
    
    let marklevel3Answers = async () => {
        answerArray = [];
        for (var i = 1; i <= 5; i++) {
            var questionDOM = document.getElementById('q' + (i).toString());
            var answerDOM = document.getElementById('a' + (i).toString());
            var partDOM = document.getElementById('part' + (i).toString());
            if (questionDOM.value == "") {
                answerDOM.style.color = "#FF0000";
                whichQuestionsCorrect.push(0);
            }
            else {
                let url = "/checkLevel3Answer" + (i).toString() + "/" + questionDOM.value;
                let answer = await fetch(url, {
                    "crossDomain": true,
                    "method": "GET"
                });
                answer = await answer.json();
                if (answer["isIdentical"] == true) {
                    whichQuestionsCorrect.push(1);
                }
                else {
                    whichQuestionsCorrect.push(0);
                }
                var html = htmlForTableGenerator(answer['userTableColumns'], answer['userTable'], questionDOM.value);
                partDOM.innerHTML += html;
            }
        }
        return whichQuestionsCorrect;
    }

    let postData = async () => {
        let url = "/submitScoreLevel3"
        let answer = await fetch(url, {
            method: 'POST',
            mode: 'cors', 
            cache: 'no-cache', 
            credentials: 'same-origin', 
            headers: {
                'Content-Type': 'application/json'
            },
            redirect: 'follow',
            referrerPolicy: 'no-referrer', 
            body: scoresInJSON
        });
        return answer.json();
    }
    
    resetButton.onclick = () => {
        location.reload();
    }

    submitButton.onclick = async () => {
        for (var i = 1; i <= 5; i++) {
            var answerDOM = document.getElementById('a' + (i).toString());
            answerDOM.style.visibility = 'visible';
        }

        resetButton.style.visibility = 'visible';
        submitButton.style.visibility = 'hidden';
        reviewButton.style.visibility = 'visible';
        
        let marked = await marklevel3Answers();
        var score = 0;
        for (var i = 0; i < marked.length; i++) {
            score = score + marked[i];
        }
        var msg = "Your score is " + score.toString() + ".";
        alert(msg);
        console.log(marked);
        console.log("Total score: ", score);

        scoresInJSObject = {"markForEach": marked, "totalScore": score};
        scoresInJSON = JSON.stringify(scoresInJSObject) 
        console.log(scoresInJSON)

        let scoreSubmitted = await postData();
        console.log(scoreSubmitted);
    }
}