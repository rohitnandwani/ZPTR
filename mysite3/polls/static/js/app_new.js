// Define the application
app = angular.module('b2', ['restangular']);

// Configure the application
app.config(function(RestangularProvider) {
    RestangularProvider.setBaseUrl(
        'http://127.0.0.1:8000/api/v1'); 
        // Note that we run everything on the localhost
});

// Define the controller
app.controller('mainCtrl', function($scope, Restangular) {
    Restangular.all('student/?format=json').getList().then(function(result) {
        $scope.student = result;
		//console.log($scope.student)
    });
	

	Restangular.all('behavior/?format=json').getList().then(function(result) {
        $scope.behavior = result;
		//console.log($scope.behavior)
    });
	
	$scope.sendForm2 = function(behaviorInput) {
        $scope.studentFormatted = {student_id: behaviorInput.student_id.student_id.toString(), student_name: behaviorInput.student_id.student_name, student_class: behaviorInput.student_id.student_class, student_age: behaviorInput.student_id.student_age.toString()};
		//$scope.studentFormatted2 = "student/" + behaviorInput.student_id.student_id

		//use auto-increment insted of random for id fields
		$scope.attendanceInsert = {attendance_id: Math.floor((Math.random() * 1000000) + 1), student: $scope.studentFormatted, attendance_date: behaviorInput.attendance_date};

        Restangular.all('attendance', $scope.attendanceInsert.attendance_id).post($scope.attendanceInsert).then(function(registerUser2) {
            console.log("Attendance Inserted");
        });
		

		var i;
		for (i = 0; i < $scope.behavior.length; i++) {
			if(behaviorInput[i] == true)
			{
				$scope.behaviorFormatted = {behavior_id : $scope.behavior[i].behavior_id, behavior_name : $scope.behavior[i].behavior_name, behavior_points: $scope.behavior[i].behavior_points}
				$scope.pointsInsert = {points_id: Math.floor((Math.random() * 1000000) + 1), student: $scope.studentFormatted, behavior: $scope.behaviorFormatted, points: $scope.behaviorFormatted.behavior_points, points_date: $scope.attendanceInsert};
				Restangular.all('points', $scope.pointsInsert.points_id).post($scope.pointsInsert).then(function(registerUser3) {
					console.log('Points inserted');
				});
			}
	
		}
	}
	
	
});

app.controller('registerCtrl', function($scope, Restangular) {
    $scope.sendForm = function(studentInput) {
        Restangular.all('student', studentInput.student_id).post(studentInput).then(function(registerUser) {
            console.log("Student Inserted");
        });
	}
});


// Standardize data format (extract from meta-data where needed)
app.config(function(RestangularProvider) {
    // add a response intereceptor
    RestangularProvider.addResponseInterceptor(function(data, operation, what, url, response, deferred) {
      var extractedData;
      //console.log(data.objects[0]);
      // .. to look for getList operations
      if (operation === "getList") {
        // .. and handle the data and meta data
        extractedData = data.objects;
      } else {
        extractedData = data;
      }
      return extractedData;
    });
});