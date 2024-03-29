
#query to search races
#take out the single backslash before name after filters
search_query = """query fetchAllRaces($name: String!) {
  response {
    success
    errors
    result {
      races (filters: {name: $name}) {
        race {
          race_id
          name
          last_date
          last_end_date
          next_date
          next_end_date
          is_draft_race
          is_private_race
          is_registration_open
          created
          last_modified
          description
          url
          external_race_url
          external_results_url
          fb_page_id
          fb_event_id
          address {
            street
            street2
            city
            state
            zipcode
            country_code
          }
          timezone
          logo_url
          real_time_notifications_enabled
        }
      }
    }
  }
}"""

advanced_search_query = """query fetchAllRaces($name: String!, $city: String!, $state: String!, $country_code: String!) {
  advancedResponse {
    success
    errors
    result {
      races(
        filters: {name: $name, city: $city, state: $state, country_code: $country_code}
      ) {
        race {
          race_id
          name
          last_date
          last_end_date
          next_date
          next_end_date
          is_draft_race
          is_private_race
          is_registration_open
          created
          last_modified
          description
          url
          external_race_url
          external_results_url
          fb_page_id
          fb_event_id
          address {
            street
            street2
            city
            state
            zipcode
            country_code
          }
          timezone
          logo_url
          real_time_notifications_enabled
        }
      }
    }
  }
}"""

single_race_query = """query fetchRace($race_id: long!) {
  race_response {
    success
    errors
    result {
      race(filters: {race_id: $race_id}) {
        race_id
        name
        last_date
        last_end_date
        next_date
        next_end_date
        is_draft_race
        is_private_race
        is_registration_open
        created
        last_modified
        description
        url
        external_race_url
        external_results_url
        fb_page_id
        fb_event_id
        address {
          street
          street2
          city
          state
          zipcode
          country_code
        }
        timezone
        logo_url
        real_time_notifications_enabled
        events {
          event_id
          race_event_days_id
          name
          details
          start_time
          end_time
          age_calc_base_date
          registration_opens
          event_type
          distance
          volunteer
          require_dob
          require_phone
          registration_periods {
            registration_opens
            registration_closes
            race_fee
            processing_fee
          }
        }
        sub_event_ids
        giveaway
      }
    }
  }
}"""

individual_results_query = """query fetchEvent($race_id: long!, $event_id: long!) {
  individual_results {
    success
    errors
    result {
      individual_results_sets(filters: {race_id: $race_id, event_id: $event_id}) {
        individual_result_set_id
      	results{
          result_id
          first_name
          last_name
          place
          bib
          chip_time
        }
      }
    }
  }
}"""

team_result_set_query = """query fetchTeamResultsSets($race_id: long!) {
  team_results_sets {
    success
    errors
    result(filters: {race_id: $race_id}) {
      team_result_set_id
      team_result_set_name
    }
  }
}"""

team_names_and_scores_query = """query fetchTeamResultsSets($race_id: long!, $team_result_set_id: long!) {
  team_scores {
    success
    errors
    result(filters: {race_id: $race_id, team_result_set_id: $team_result_set_id}) {
      results_team_name
      place
      score
    }
  }
}"""

updated_events_and_teams_query = """query fetchTeamIDandEvents($race_id: long!) {
  team_results_sets{
    success
    errors
    result(filters: {race_id: $race_id}){
      team_result_set_id
      team_result_set_name
    }
  }
  race_response {
    success
    errors
    result {
      race(filters: {race_id: $race_id}) {
        race_id
        name
        last_date
        last_end_date
        next_date
        next_end_date
        is_draft_race
        is_private_race
        is_registration_open
        created
        last_modified
        description
        url
        external_race_url
        external_results_url
        fb_page_id
        fb_event_id
        address {
          street
          street2
          city
          state
          zipcode
          country_code
        }
        timezone
        logo_url
        real_time_notifications_enabled
        events {
          event_id
          race_event_days_id
          name
          details
          start_time
          end_time
          age_calc_base_date
          registration_opens
          event_type
          distance
          volunteer
          require_dob
          require_phone
          registration_periods {
            registration_opens
            registration_closes
            race_fee
            processing_fee
          }
        }
        sub_event_ids
        giveaway
      }
    }
  }
}"""

individual_results_query_frontend = """
query fetchTest($race_id: long!, $event_id: long!) {
  frontend_call {
    success
    errors
    result {
      individual_results_sets(filters: {race_id: $race_id, event_id: $event_id}) {
        individual_result_set_id
      	results{
          result_id
          first_name
          last_name
          place
          bib
          chip_time
        }
      }
    }
  }
}"""