flag=1,L.mapbox.accessToken="pk.eyJ1IjoieGlhb2xpIiwiYSI6IkhpWkZhZFkifQ.RgWs4kq33jfD3d46_TTd6g";var map=L.mapbox.map("map","examples.map-i86nkdio").setView([52.3648367,4.9151507],13),marker=L.marker([52.3648367,4.9151507],{icon:L.mapbox.marker.icon({"marker-color":"#9c89cc"})}).bindPopup("<p>Halloooo~</p>").addTo(map);marker.on("click",function(a){showHideBoard()});var showHideBoard=function(){$(".board").animate(flag?{"margin-right":"-=300"}:{"margin-right":"+=300"}),console.log(flag),flag=flag?0:1};