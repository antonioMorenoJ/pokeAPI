import { Component } from '@angular/core';
import {MatFormFieldModule} from '@angular/material/form-field';
import { FormsModule } from '@angular/forms';
import {MatInputModule} from '@angular/material/input';
import { MatButtonModule } from '@angular/material/button';
import { PokemonService } from '../services/pokemon.service';
import {MatTableModule} from '@angular/material/table';
import { CommonModule } from '@angular/common';
import { MatCardModule } from '@angular/material/card';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-pokemon',
  standalone: true,
  imports: [MatFormFieldModule, MatInputModule, MatButtonModule, FormsModule, MatTableModule, CommonModule, MatCardModule],
  templateUrl: './pokemon.component.html',
  styleUrl: './pokemon.component.scss'
})
export class PokemonComponent {
  pokemon_info: any[] = [];
  pokemon_name: string = '';
  displayedColumns: string[] = ['pokemon', 'move', 'type', 'generation', 'image_url'];  

  constructor(private pokemonService: PokemonService) { }

  ngOnInit() {
    console.log("Pokemon component initialized");
  }

// search pokemon 
  searchPokemon() {
      this.pokemonService.getPokemons(this.pokemon_name).subscribe(
        (data)=>{
          if(Array.isArray(data)){
            this.pokemon_info = data;
          }else{
            this.pokemon_info = [data];
          }
          console.log("Datos", this.pokemon_info);
        },
        (error)=>{
          console.log("Error", error);
          }
      )
        
      
  }


  cleanTable() {
    //remove all the data from the table
    this.pokemon_info = [];
    //load all the data from the database
    //this.loadAllPokemon();
    //clear the search field
    this.pokemon_name = '';
    //clear the search field

  }

}
