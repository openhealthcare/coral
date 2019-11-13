angular.module('opal.services').service('DiagnosisRecord', function($window){
    return function(item){
      if(!item.date_of_diagnosis){
          item.date_of_diagnosis = moment();
      }
    };
});
