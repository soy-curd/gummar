
// 画面サイズ等。アドホックに決める
var w = 1024;
var h = 768/2 + 130;
var fontSize = 30;
var margine = 5;
var sentencederay = 300;
var sentenceduration = 20000;
var graphdelay = 100;
var graphduration = 20000;
var barwidth = 5;

//xmlを読み込んでグラフと文字を描写する
readXml();

function readXml () {
  d3.xml("xml/novel.xml","application/xml", function(xml){
      var word = xml.documentElement.getElementsByTagName("word");
      var text = "";
      var lSurface = [];
      var lNum = [];
      var list = [];

      // wordタグの数だけ処理
      for(var i=0; i<word.length; i++){
          var surface = word[i].getElementsByTagName("surface");
          var num = word[i].getElementsByTagName("feature");
          list.push([word[i].getElementsByTagName("surface"),
                     word[i].getElementsByTagName("feature")]);
      }
      //文字を読みやすいように文に変換
      lSentence = word2sentence(list);

      //文字とグラフの描画
      drawSentence(lSentence);
  });
}


// 単語を文にする。
//
// IN [[単語, score], ...]
//
// OUT [[文, Σ(score)/単語数, [score, score, ... ]], ...]
//
function word2sentence (list) {
  sentence = "";
  score = 0;
  lWordScore = [];
  wordNum = 0;
  lSentence = [];

  for (var i=0; i<list.length; i++ , wordNum++) {
    sentence += list[i][0][0].firstChild.nodeValue;
    score += parseInt(list[i][1][0].firstChild.nodeValue);
    lWordScore.push(list[i][1][0].firstChild.nodeValue)

    //"。""、"で区切る。
    if (list[i][0][0].firstChild.nodeValue == "。" ||
          list[i][0][0].firstChild.nodeValue == "、" ) {
        lSentence.push([sentence,
                          String(Math.round(score/wordNum)),
                          lWordScore])
        sentence = "";
        score = 0;
        wordNum = 0;
        lWordScore = [];
    }
  }

  return lSentence;
}

function drawSentence(list) {

  // ランダムな配列（文字のレイアウト用）
  var lNum = allocateNum(20);

  // 背景
  var svg = d3.select("#example")
    .style("background-color", "black")
    .append("svg")
    .attr({
      width: w,
      height: h,
    })
    ;

  //　タイトル
  var titleText = svg
    .append("text")
    .text("Dynamics of Japanese Text")
    .attr("x", 10)
    .attr("y", 50)
    .attr("font-size", 50)
    .attr("fill", "#00ff00")
    ;

  // lineの設定
  // 横方向はSVG領域に合わせて調整。データは最低2個あるのが前提
  // 縦方向は数値そのままでスケール等しない
  var line = d3.svg.line()
    .x(function(d, i){ return i * w/(d.length-1); })
    .y(function(d){ return h-d; })

  // グラフを描写
  // data()メソッドを呼ぶことで、その後にチェインされたメソッドの中で、
  // d を入力値として受け取れる無名関数が使えるようになる。
  var graph = svg.selectAll(".bar")
    .data(list)
    .enter()
    .append("rect")
    .attr("class", "bar")
    .attr("x", w)
    .attr("width", barwidth)
    .attr("y", function(d) { return h/4 - d[1] + 50; })
    .attr("height", function(d) { return d[1]; })
    .attr("fill", "#00ff00")

    .transition()
    .duration(graphduration)
    .delay(function(d, i) {return i*sentencederay;})
    .attr("x", - 0.2*w)
    .ease("linear")
    ;

  var text = svg.selectAll("text")
     .data(list)
     .enter()
     .append("text")
     .text(function(d) {return d[0];})
     .attr("x", w)
     .attr("y", function(d, i) {return h/2 +
         (lNum[i%lNum.length] * (h/2)/10) ;})
     .attr("font-size", function(d) {return getFontSize(d[1]);})
     .attr("fill", "#00ff00")
     ;

   // ランダムな配列を作成する
  function allocateNum (n) {
    var lNum = [];

    for (var i = 0; i < n ; i++) {
      lNum.push(i);
    }
    // 配列の中身をランダムに並び替える
    lNum.sort(
        function() {return Math.random() - 0.5;}
    );
    return lNum;
  }

  function getFontSize(n) {
    return fontSize * n/ 100;
  }

  function moveText(text, graph){
    text
    .transition()
    .delay(function(d, i) {return i*sentencederay;})
    .duration(sentenceduration)
    .ease("line")
    .attrTween(
     // アニメーションする
      'x', function(d,i) {
        // tはeaseで設定
        return function(t) {return 1.4 * (w - t * w) - 0.2*w;};
        }
    )
    .each("end", function() {d3.select(this).remove();})
    ;

    graph;
  }

  titleText;
  moveText(text, graph);
}
