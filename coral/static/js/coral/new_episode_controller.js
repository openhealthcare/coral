angular.module('opal.controllers').controller(
    'NewEpisodeModalCtrl',
    function($scope, $modalInstance, patient_id) {

        $scope.patient_id = patient_id;

	$scope.cancel = function() {
	    $modalInstance.close('cancel');
	};
});
